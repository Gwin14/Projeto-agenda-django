from django.shortcuts import render

from contact.models import Contact

# Create your views here.


def index(request):

    contacts = Contact.objects.all().filter(show=True).order_by('id')

    context = {
        'contacts': contacts,
        'sitetitle': 'Contatos - '
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
