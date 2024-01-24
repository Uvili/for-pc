from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def contact_submit(request):
    if request.method == 'GET':
        return redirect(request,'contact.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, email, phone, message)
        contact = Contact.objects.create(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'contact.html', {'contact' : contact})