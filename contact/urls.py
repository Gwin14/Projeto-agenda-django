from django.urls import path
from contact import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    # CRUD
    path('contact/detail/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]
