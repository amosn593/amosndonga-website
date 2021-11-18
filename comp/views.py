from repair.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .models import Messages

# Create your views here.

# Home view


def index(request):
    if request.method == 'GET':
        return render(request, "comp/index/index.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")

# About view


def profile(request):
    if request.method == 'GET':
        return render(request, "comp/about/about.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


# Services view
def service(request):
    if request.method == 'GET':
        return render(request, "comp/services/services.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


# Product view
def products(request):
    if request.method == 'GET':
        return render(request, "comp/product/product.html")
    else:
        return HttpResponse("INVALID HTTP METHOD")


# Contact view
def contact(request):
    if request.method == 'GET':
        return render(request, 'comp/contact/contact.html')
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name').strip()
        phone = request.POST.get('phone').strip()
        email = request.POST.get('email').strip()
        message = request.POST.get('message').strip()

        # Send user email acknowledging receipt of the message

        body = f"Dear {name},\n\nWe acknowledge the receipt of your email. \n\n About: \n {message} \n\n. We will get back to you very soon.\n\n Kind Regards\nAMOS ICT SERVICES\ninfo@amosndonga.com\namosndonga@gmail.com \n 0702240787."

        subject = f"Client email - {name} - {phone}- {email}"

        try:
            m = Messages(full_name=name, phone=phone,
                         email=email, message=message)

            m.save()

            send_mail(subject,
                      body, EMAIL_HOST_USER, [email, 'amosndonga@gmail.com'], fail_silently=False)
            # Flash message to user
            message = 'Message sent successfully!'
            return HttpResponse(message)
        except:
            # Flash message to user
            message = 'Message not sent!'
            return HttpResponse(message)
    else:
        message = 'Something went wrong!!!'
        return HttpResponse(message)


# Contact view
