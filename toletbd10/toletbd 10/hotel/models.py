from django.db import models
from PIL import Image
from users.models import CustomUser as User

class MainContent(models.Model):
    heading = models.CharField(max_length=60)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='mainpic/')

    def __str__(self):
        return self.heading

class Our_Property(models.Model):
    image = models.ImageField(upload_to='our_property/')
    heading = models.CharField(max_length=60)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading
    
class Why_Book(models.Model):
    image = models.ImageField(upload_to='why_book/')
    heading = models.CharField(max_length=60)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading

class Guest_Think(models.Model):
    image = models.ImageField(upload_to='guest_think/')
    heading = models.CharField(max_length=60)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
       
class Shorts(models.Model):
    image = models.ImageField(upload_to='shorts/')
    heading = models.CharField(max_length=60)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading
    
class Asked_Questions(models.Model):
    heading = models.CharField(max_length=60)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading
    
class Asked_Questions_Form(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname + " - " + self.email

class Sponsers(models.Model):
    brande_name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='sponsers/')
    brande_link = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.brande_name
    
class Newsletter(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class About_Desc(models.Model):
    head = models.CharField(max_length=100)
    para = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.head
    
class ManagementTeam(models.Model):
    image = models.ImageField(upload_to='about/management/')
    fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname

class About_Developers(models.Model):
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/developer/', default='media/no-image.png')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    icon1 = models.ImageField(upload_to='about/icons/', null=True, blank=True)
    url1 = models.CharField(max_length=225, null=True, blank=True)
    icon2 = models.ImageField(upload_to='about/icons/', null=True, blank=True)
    url2 = models.CharField(max_length=225, null=True, blank=True)
    icon3 = models.ImageField(upload_to='about/icons/', null=True, blank=True)
    url3 = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + "  -  " + self.role

class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField()
    
    def __str__(self):
        return self.first_name + "  -  " + self.email

class Division(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    country = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Upazila(models.Model):
    state = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name


class LatestNews(models.Model):
    CHOICES = [
        ('Family', 'Family'),
        ('Sublet', 'Sublet'),
        ('Bachelor', 'Bachelor'),
        ('Hostel', 'Hostel'),
        ('Office', 'Office'),
        ('Shop', 'Shop'),
    ]
    
    OFFER_CHOICES = [
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    ]
    
    PROPERTY_CHOICES = [
        ('Owner', 'Owner'),
        ('Apartment', 'Apartment'),
    ]
    
    BUILDING_AGE_CHOICES = [
        ('0 to 10', '0 to 10'),
        ('11 to 20', '11 to 20'),
        ('20 up', '20 up'),
    ]
    
    BED_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    WASH_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    BALCONY_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    
    GAS_CHOICES = [
        ('LPG', 'LPG'),
        ('Supply Gas', 'Supply Gas'),
    ]
    
    ELECTRICITY_CHOICES = [
        ('Prepaid', 'Prepaid'),
        ('Postpaid', 'Postpaid'),
    ]
    
    radiocheck = models.CharField(max_length=10, choices=CHOICES, blank=True, null=True)
    property_title = models.CharField(max_length=60)
    floor_number = models.CharField(max_length=60)
    flat_size = models.CharField(max_length=60)
    price = models.CharField(max_length=10)
    service_charge = models.CharField(max_length=10, blank=True, null=True)
    offer_for = models.CharField(max_length=10, choices=OFFER_CHOICES)
    property_type = models.CharField(max_length=10, choices=PROPERTY_CHOICES)
    building_age = models.CharField(max_length=10, choices=BUILDING_AGE_CHOICES)
    bed = models.CharField(max_length=1, choices=BED_CHOICES)
    wash = models.CharField(max_length=1, choices=WASH_CHOICES)
    balcony = models.CharField(max_length=1, choices=BALCONY_CHOICES, blank=True, null=True)
    gas = models.CharField(max_length=10, choices=GAS_CHOICES)
    electricity = models.CharField(max_length=10, choices=ELECTRICITY_CHOICES)
    
    security = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    fire = models.BooleanField(default=False)
    generator = models.BooleanField(default=False)
    
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    
    image = models.ImageField(upload_to='latest_news/', blank=True, null=True)
    desc = models.TextField(max_length=60)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.property_title} - {self.radiocheck}"
class LatestNewsImage(models.Model):
    property = models.ForeignKey(LatestNews, on_delete=models.CASCADE)
    image = models.FileField(upload_to='latest_news_images')

    def __str__(self):
        return self.property.property_title
    
    class Meta:
        verbose_name = "LatestNews Images"


class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = [
        ('Family', 'Family'),
        ('Sublet', 'Sublet'),
        ('Bachelor', 'Bachelor'),
        ('Hostel', 'Hostel'),
        ('Office', 'Office'),
        ('Shop', 'Shop'),
    ]
    
    OFFER_CHOICES = [
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    ]
    
    PROPERTY_CHOICES = [
        ('Owner', 'Owner'),
        ('Apartment', 'Apartment'),
    ]
    
    BUILDING_AGE_CHOICES = [
        ('0 to 10', '0 to 10'),
        ('11 to 20', '11 to 20'),
        ('20 up', '20 up'),
    ]
    
    BED_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    WASH_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    BALCONY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    
    GAS_CHOICES = [
        ('LPG', 'LPG'),
        ('Supply Gas', 'Supply Gas'),
    ]
    
    ELECTRICITY_CHOICES = [
        ('Prepaid', 'Prepaid'),
        ('Postpaid', 'Postpaid'),
    ]
    
    radiocheck = models.CharField(max_length=10, choices=CHOICES, blank=True, null=True)
    property_title = models.CharField(max_length=60)
    floor_number = models.CharField(max_length=60)
    flat_size = models.CharField(max_length=60)
    price = models.CharField(max_length=10)
    service_charge = models.CharField(max_length=10, blank=True, null=True)
    offer_for = models.CharField(max_length=10, choices=OFFER_CHOICES)
    property_type = models.CharField(max_length=10, choices=PROPERTY_CHOICES)
    building_age = models.CharField(max_length=10, choices=BUILDING_AGE_CHOICES)
    bed = models.CharField(max_length=1, choices=BED_CHOICES)
    wash = models.CharField(max_length=1, choices=WASH_CHOICES)
    balcony = models.CharField(max_length=1, choices=BALCONY_CHOICES, blank=True, null=True)
    gas = models.CharField(max_length=10, choices=GAS_CHOICES)
    electricity = models.CharField(max_length=10, choices=ELECTRICITY_CHOICES)
    
    security = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    fire = models.BooleanField(default=False)
    generator = models.BooleanField(default=False)
    
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    
    image = models.ImageField(upload_to='property/', default='no-image.png')
    desc = models.TextField(max_length=60)

    family_member = models.CharField(max_length=20, blank=True, null=True)
    sublet_member = models.CharField(max_length=20, blank=True, null=True)
    bachelor_seats = models.CharField(max_length=20, blank=True, null=True)
    hostel_seats = models.CharField(max_length=20, blank=True, null=True)
    hostel_quality = models.CharField(max_length=20, blank=True, null=True)
    hostel_plan = models.FileField(upload_to='floor_plan', max_length=100, blank=True, null=True)
    office_seats = models.CharField(max_length=20, blank=True, null=True)
    shop_quality = models.CharField(max_length=20, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.property_title} - {self.radiocheck}"
    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.FileField(upload_to='property_images')

    def __str__(self):
        return self.property.property_title
    
    class Meta:
        verbose_name = "Property Images"