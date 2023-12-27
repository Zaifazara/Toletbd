from django.urls import path
from users import views
from django.contrib.auth import views as auth_views


# create routes here
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('card/', views.card_details, name='card'),

    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user-dashboard/user-cancellation/',
         views.user_cancellation, name='user-cancellation'),
    path('user-dashboard/user-report/', views.user_report, name='user-report'),
    
    path('user-dashboard/user-profile/',
         views.user_profile, name='user-profile'),
    path('user-dashboard/user-edit-profile/',
         views.user_edit_profile, name='user-edit-profile'),
    path('user-dashboard/user-pass-change/',
         views.user_pass_change, name='user-edit-profile'),

    path('user-dashboard/user-support/',
         views.user_support, name='user-support'),
    path('user-dashboard/user-tickets/',
         views.user_tickets, name='user-tickets'),
    path('user-dashboard/add-tickets/',
         views.add_tickets, name='add-tickets'),
    
    path('password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-done/', views.password_reset_done,
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.password_reset_confirm, name='password_reset_confirm'),
    path('password-reset-complete/', views.password_reset_complete,
         name='password_reset_complete'),
    
    path('get-districts/', views.get_districts, name='get_districts'),
    path('get-upazilas/', views.get_upazilas, name='get_upazilas'),
]
