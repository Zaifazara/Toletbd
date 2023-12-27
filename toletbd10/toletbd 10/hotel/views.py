from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hotel.forms import *
from hotel.models import *
from users.models import *
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    maincontent = MainContent.objects.all()
    our_property = Our_Property.objects.all()
    why_book = Why_Book.objects.all()
    guest = Guest_Think.objects.all()
    short = Shorts.objects.all()
    asked_questions = Asked_Questions.objects.all()
    latest = LatestNews.objects.all()
    latest_news_images = LatestNewsImage.objects.all()
    sponsers = Sponsers.objects.all()
    

    if request.method == 'POST':
        form = Asked_Questions_Form_Forms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your questions were submitted successfully.")
        else:
            messages.error(request, "Failed to submit your questions. Please check the form data.")
    else:
        form = Asked_Questions_Form_Forms()
    

    context = {
        'maincontent': maincontent,
        'our_property': our_property,
        'why_book': why_book,
        'guest': guest,
        'short': short,
        'ask': asked_questions,
        'latest':latest,
        'latest_images':latest_news_images,
        'sponsers': sponsers,
    }
    return render(request, 'index.html', context)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your questions were submitted successfully.")
        else:
            messages.error(request, "Failed to submit your questions. Please check the form data.")
    messages.info(request, 'Please enter your mail.')
    return redirect('home')


def about(request):
    desc = About_Desc.objects.all()
    management = ManagementTeam.objects.all()
    developers = About_Developers.objects.all()
    
    context = {
        'desc': desc,
        'managements': management,
        'developers': developers,
    }
    return render(request, 'hotel/about.html', context)


def contact(request):
    maincontent = MainContent.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "Failed to send message!!")
    else:
        form = ContactForm()
            
    return render(request, 'hotel/contact.html', {'maincontent': maincontent,})


@login_required(login_url='signin')
def property_list(request):
    property_images = PropertyImage.objects.all()
    
    if request.method == 'GET':
        radiocheck = request.GET.get('radiocheck')
        offer_for = request.GET.get('offer_for')
        if radiocheck:
            properties = Property.objects.filter(radiocheck=radiocheck)
        elif offer_for:
            properties = Property.objects.filter(offer_for=offer_for)
        else:
            properties = Property.objects.all()
    return render(request, 'hotel/property_list.html', {'property':properties, 'allimg':property_images})

@login_required(login_url='signin')
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.user = request.user
            property_instance.save()
            messages.success(request, 'Posted successfully')
            return redirect('property-list')
        else:
            messages.error(request, 'Invalid form data. Please, fill all information.')
    else:
        form = PropertyForm()

    divisions = Division.objects.all()
    context = {
        'divisions': divisions,
        'form': form,
    }
    return render(request, 'hotel/add_property.html', context)

@login_required(login_url='signin')
def card_details(request, id):
    property = Property.objects.get(id=id)
    property_images = PropertyImage.objects.filter(property=property)
    return render(request, 'hotel/card_details.html', {'p':property, 'allimg':property_images})

def terms(request):
    return render(request, 'terms-privacy/terms.html')

def privacy(request):
    return render(request, 'terms-privacy/privacy.html')


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
