from repair.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
# from .models import Messages

# Create your views here.

#Home view
def index(request):
    return render(request, "comp/index/index.html")

#About view
def profile(request):
    return render(request, "comp/about/about.html")


# Services view
def service(request):
    return render(request, "comp/services/services.html")


# Product view
def products(request):
    return render(request, "comp/product/product.html")


#Contact view
def contact(request):
    return render(request, 'comp/contact/contact.html')
   
#Contact view
def contact_back(request):           
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        #Send user email acknowledging receipt of the message
        
        body = f"Dear {name},\n\nWe acknowledge the receipt of your email. \n\n About: \n {message} \n\n. We will get back to you very soon.\n\n Kind Regards\n\namosndonga@gmail.com \n 0702240787."
        
        subject = f"Client email - {name} - {phone}- {email}"
        
        
        try:
        
            send_mail(subject, 
                body, EMAIL_HOST_USER, [email,'amosndonga@gmail.com'], fail_silently = False)
            #Flash message to user
            message = 'Message sent successfully!'
            return HttpResponse(message)
        except:
            #Flash message to user
            message = 'Message not sent!'
            return HttpResponse(message)
    else:
        message = 'Something went wrong!!!'
        return HttpResponse(message)
        
    




