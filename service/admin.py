from django.contrib import admin
from . models import service,ServiceSubMenu,subservices,sub_expertise,subproject,headbanner,expertise,sub_expertise_icon,WhatWeDo,serviceFact,sub_benifit,sub_serviceWeOffer,devLifecycle,engagement,expertiseWithTitleIcon,middleimage,bottomdiv




class headbannerAdmin(admin.ModelAdmin):
    list_display = ('service','sub_service')

class subprojectAdmin(admin.ModelAdmin):
    list_display = ('services','project_type','name')

class sub_expertiseAdmin(admin.ModelAdmin):
    list_display = ('subservices','expertise')
class sub_serviceWeOfferAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class sub_benifitAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class ServiceSubMenuAdmin(admin.ModelAdmin):
    list_display = ('service','Submenu')
class expertiseAdmin(admin.ModelAdmin):
    list_display = ('services','Select_type')

class sub_expertise_iconAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class expertiseWithTitleIconAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class WhatWeDoAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class serviceFactAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class devLifecycleAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class engagementAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class middleimageAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')
class bottomdivAdmin(admin.ModelAdmin):
    list_display = ('services','subservices')



# Register your models here.
admin.site.register(service)
admin.site.register(ServiceSubMenu,ServiceSubMenuAdmin)
admin.site.register(middleimage,middleimageAdmin)
admin.site.register(subservices)
admin.site.register(expertise,expertiseAdmin)
admin.site.register(bottomdiv,bottomdivAdmin)
admin.site.register(sub_expertise_icon, sub_expertise_iconAdmin)
admin.site.register(WhatWeDo,WhatWeDoAdmin)
admin.site.register(devLifecycle,devLifecycleAdmin)
admin.site.register(sub_serviceWeOffer,sub_serviceWeOfferAdmin)
admin.site.register(sub_benifit,sub_benifitAdmin)
admin.site.register(serviceFact,serviceFactAdmin)
admin.site.register(expertiseWithTitleIcon,expertiseWithTitleIconAdmin)
admin.site.register(engagement,engagementAdmin)
admin.site.register(sub_expertise,sub_expertiseAdmin)
admin.site.register(subproject,subprojectAdmin)
admin.site.register(headbanner,headbannerAdmin)