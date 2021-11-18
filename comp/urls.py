from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("profile/", views.profile, name='profile'),
    path("our-services/", views.service, name='services'),
    path("contact-us/", views.contact, name='contact'),
    # path("products/", views.products, name = 'products'),
]
