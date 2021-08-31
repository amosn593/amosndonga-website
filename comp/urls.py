from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name = 'home'),
    path("profile/", views.profile, name = 'profile'),
    path("services/", views.service, name = 'services'),
    path("contact/", views.contact, name = 'contact'),
    path("contact_back/", views.contact_back, name = 'contact_back'),
    # path("products/", views.products, name = 'products'),
]