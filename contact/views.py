from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from contact.models import Contact
from contact.forms import ContactForm
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


def create(request):
    form_action = reverse('create')

    if request.method == 'POST':

        form = ContactForm(request.POST)

        context = {
            'sitetitle': 'Criar - ',
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
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context=context
    )


def update(request, contact_id):
    contact = Contact.objects.get(pk=contact_id, show=True)

    form_action = reverse('update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST, instance=contact)

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
