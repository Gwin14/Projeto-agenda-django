from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from contact.models import Contact
from contact.forms import ContactForm

from contact.forms import RegisterForm, RegisterUpdateForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.


def index(request):

    contacts = Contact.objects.filter(show=True).order_by('id')

    context = {
        'contacts': contacts,
        'sitetitle': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )


@login_required(login_url='login')
def create(request):
    form_action = reverse('create')

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)

        context = {
            'sitetitle': 'Criar - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context
        )

    context = {
        'sitetitle': 'Criar - ',
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )


@login_required(login_url='login')
def update(request, contact_id):
    contact = Contact.objects.get(pk=contact_id, show=True, owner=request.user)

    form_action = reverse('update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'sitetitle': 'Atualizar - ',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context
        )

    context = {
        'sitetitle': 'Criar - ',
        'form': ContactForm(instance=contact)
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )


@login_required(login_url='login')
def delete(request, contact_id):
    contact = Contact.objects.get(pk=contact_id, show=True)
    contact.delete()
    return redirect('index')


def search(request):

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('id')

    context = {
        'contacts': contacts,
        'sitetitle': 'Resultado de pesquisa - '
    }

    return render(
        request,
        'contact/index.html',
        context=context
    )


def contact(request, contact_id):

    single_contact = Contact.objects.get(pk=contact_id)

    context = {
        'contact': single_contact,
        'sitetitle': single_contact.first_name + '' + single_contact.last_name+' - ',
    }

    return render(
        request,
        'contact/contact.html',
        context=context
    )


# USER FORMS

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context=context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context=context
    )


@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form': form
            }
        )

    form.save()
    return redirect('user_update')
