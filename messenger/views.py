from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.contrib import messages as info

def messages(request):
    if request.method == 'POST':

        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        c=Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.messages=message
        c.save()

        info.success(request, 'Message sent successfully.')
    return render(request,'contact.html')
def messages_list(request):
    contact=Contact.objects.all()
    return render(request,'messages_list.html',{'contact':contact})


def get_message(request,id):
    instance=get_object_or_404(Contact,id=id)

    return render(request,'message.html',{'instance':instance})
