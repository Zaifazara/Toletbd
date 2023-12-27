from django.contrib import admin
from hotel.models import *

admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)

admin.site.register(MainContent)
admin.site.register(Our_Property)
admin.site.register(Why_Book)
admin.site.register(Guest_Think)
admin.site.register(Shorts)
admin.site.register(Asked_Questions)
admin.site.register(Asked_Questions_Form)
admin.site.register(Sponsers)
admin.site.register(Newsletter)

admin.site.register(Contact)

admin.site.register(About_Desc)
admin.site.register(ManagementTeam)
admin.site.register(About_Developers)

class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage
    min_num = 0
    extra = 1
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

admin.site.register(Property, PropertyAdmin)

class LatestNewsImageAdmin(admin.StackedInline):
    model = LatestNewsImage
    min_num = 0
    extra = 1
class LatestNewsAdmin(admin.ModelAdmin):
    inlines = [LatestNewsImageAdmin]

admin.site.register(LatestNews, LatestNewsAdmin)