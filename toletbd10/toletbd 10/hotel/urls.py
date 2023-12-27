from django.urls import path
from hotel import views


#create urls here
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('property-list/', views.property_list, name='property-list'),
    path('card-details/<int:id>', views.card_details, name='card-details'),
    path('newsletter/', views.newsletter, name="newsletter"),
    path('add-property/', views.add_property, name='add-property'),

    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),

    path('get-districts/', views.get_districts, name='get_districts'),
    path('get-upazilas/', views.get_upazilas, name='get_upazilas'),
]
