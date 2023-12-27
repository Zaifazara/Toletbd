from django.shortcuts import render, redirect
from users.forms import *
from users.models import *
from hotel.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.template.loader import render_to_string
from email.message import EmailMessage
from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from hotelmanagement.settings import DEFAULT_FROM_EMAIL

UserModel = get_user_model()

def signup(request):  
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully signup.')
            return redirect('signin')
        else:
            messages.error(request, 'Email alredy exist. Please use another email. ')
    else:
        form = RegistrationForm()
    return render(request, 'users/signup.html')


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            messages.warning(request, 'Incorrect email or password.')
            return render(request, 'users/login.html')
        else:
            messages.warning(request, 'Incorrect email or password.')
            return redirect('signin')
    else:
        form = LoginForm()
    return render(request, 'users/login.html')


@login_required(login_url='signin')
def log_out(request):
    logout(request)
    messages.success(request, 'User successfully logout.')
    return redirect('home')


@login_required(login_url='signin')
def card_details(request):
    return render(request, 'card_details.html')


@login_required(login_url='signin')
def user_dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required(login_url='signin')
def user_cancellation(request):
    return render(request, 'dashboard/dashboard_cancellation.html')


@login_required(login_url='signin')
def user_report(request):
    if request.method == 'POST':
        form = ReportIssueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your report submitted!')
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Please fill all details.')
    else:
        form = ReportIssueForm()

    return render(request, 'dashboard/dashboard_report_issue.html')


@login_required(login_url='signin')
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'dashboard/dashboard_profile.html', {'profile': profile})


@login_required(login_url='signin')
def user_edit_profile(request):
    divisions = Division.objects.all()
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile updated sucessfully!")
            return redirect('user-profile')
        else:
            messages.error(request, "fill the forms corectly!")
    else:
        form = ProfileForm(instance=user_profile)

    context = {
        'form': form,
        'divisions':divisions
    }
    return render(request, 'dashboard/dashboard_edit_profile.html', context)


@login_required(login_url='signin')
def user_pass_change(request):
    user = get_user(request)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            profile.last_password_update = timezone.now()
            profile.save()
            messages.success(request, "Password Changed successfully!")
            return redirect('user-profile')
        else:
            messages.error(request, "Please enter correct password.")
    else:
        form = SetPasswordForm(user)

    return render(request, 'dashboard/dashboard_pass_change.html', {'form': form})


# Dashboard Support
@login_required(login_url='signin')
def user_support(request):
    profile = Profile.objects.get(user=request.user)
    ticket = Ticket.objects.all()
    context = {
        'profile': profile,
        'tickets':ticket
        }
    return render(request, 'dashboard/dashboard_support.html',context)

@login_required(login_url='signin')
def user_tickets(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'dashboard/dashboard_tickets.html', {'profile': profile})


@login_required(login_url='signin')
def add_tickets(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ticket submitted successfully!")
            return redirect('user-support')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        form = TicketForm()
    return render(request, 'dashboard/dashboard_add_tickets.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = reverse('password_reset_confirm', args=(uid, token))
            current_site = get_current_site(request)
            mail_subject = 'Password Reset Request'
            message = render_to_string('users/password_reset_email.html', {
                'user': user,
                'domain': current_site.domain,
                'reset_link': reset_link,
                'uid': uid,
                'token': token,
            })

            send_mail(mail_subject, message, DEFAULT_FROM_EMAIL,
                      [email], fail_silently=False)
        return render(request, 'users/password_reset_done.html')
    return render(request, 'users/password_reset_form.html')


def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            user.set_password(new_password)
            user.save()
            return render(request, 'users/password_reset_complete.html')
        return render(request, 'users/password_reset_confirm.html')
    else:
        return HttpResponse('Password reset link is invalid')


def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')


def password_reset_complete(request):
    return render(request, 'users/password_reset_complete.html')


def get_districts(request):
    division_id = request.GET.get('division_id')
    districts = District.objects.filter(country_id=division_id)
    data = [{'id': district.id, 'name': district.name} for district in districts]
    return JsonResponse({'districts': data})

def get_upazilas(request):
    district_id = request.GET.get('district_id')
    upazilas = Upazila.objects.filter(state_id=district_id)
    data = [{'id': upazila.id, 'name': upazila.name} for upazila in upazilas]
    return JsonResponse({'upazilas': data})
