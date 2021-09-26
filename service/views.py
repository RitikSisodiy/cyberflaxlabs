from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import service,ServiceSubMenu,headbanner,subservices,subproject,expertise,sub_expertise,sub_expertise_icon,sub_benifit,WhatWeDo,serviceFact,sub_serviceWeOffer,ServiceSubMenu,devLifecycle,engagement,expertiseWithTitleIcon,middleimage,bottomdiv

from random import randint 
# Create your views here.
def services(request , num1=0):
	return render(request,'service/service.html')
def handle(request,num1,num2= 0):
	if type(num1)==str:
		num1 = num1.replace('__','/')
		try:
			num1 =  service.objects.get(title = num1.replace('_',' ')).id
		except Exception as a:
			return redirect('home')
	if type(num2)==str:
		num2 = num2.replace('__','/')
		try:
			num2 =  ServiceSubMenu.objects.get(Submenu = num2.replace('_',' ')).id
		except Exception as a:
			return redirect('home')
	cats=[]
	if num2 == 0:
		Service = ServiceSubMenu.objects.filter(service=num1)
		cats= []
		if len(Service)>0:
			cat= []
			for i in Service:
				banner = headbanner.objects.get(service=num1, sub_service= i.id)
				up = {}
				up['id'] = 	i.id	
				up['title'] = 	str(i.Submenu)	
				up['content'] = banner.banner_content	
				up['icon'] = 	banner.banner_icon
				cat.append(up)
			cats = [Service[0].service,cat]	
		Service = ServiceSubMenu.objects.filter(Submenu='none')
		num2= Service[0].id
		title = service.objects.get(id=num1).title
	else:
		title = ServiceSubMenu.objects.get(id=num2).Submenu
	banner = headbanner.objects.filter(service = num1 , sub_service= num2)
	Subservice = subservices.objects.filter(service = num1 , sub_service = num2)
	Subproject = subproject.objects.filter(services=num1,project_type = num2)
	Sub_expertise = sub_expertise.objects.filter(services=num1,subservices = num2)
	Expertise = expertise.objects.filter(services=num1,Select_type = num2)
	Sub_expertise_icon= []
	ExpertiseWithTitleIcon=[]
	if len(Expertise)>0:
		Sub_expertise_icon = sub_expertise_icon.objects.filter(services=num1,subservices =num2)
		ExpertiseWithTitleIcon = expertiseWithTitleIcon.objects.filter(services=num1,subservices = num2)
	whatWeDo = WhatWeDo.objects.filter(services=num1,subservices = num2)
	ServiceFact = serviceFact.objects.filter(services=num1,subservices = num2)
	Sub_benifit = sub_benifit.objects.filter(services=num1,subservices = num2)	
	Sub_serviceWeOffer = sub_serviceWeOffer.objects.filter(services=num1,subservices = num2)
	DevLifecycle=[]
	DevLifecycle = devLifecycle.objects.filter(services=num1,subservices = num2)
	Engagement = engagement.objects.filter(services=num1,subservices = num2)
	Middleimage = middleimage.objects.filter(services=num1,subservices = num2)
	Bottomdiv = bottomdiv.objects.filter(services=num1,subservices = num2)
	res = str(num1)+' '+str(num2)
	res = {
		'title': title,
		'ourservice':'active',
		'responce':res,
		'banner':banner,
		'sub_service': Subservice,
		'Subproject': Subproject,
		'expertise': [Sub_expertise,len(Sub_expertise)//2 +1 , Expertise , Sub_expertise_icon,ExpertiseWithTitleIcon],
		'whatwedo' : whatWeDo,
		'fact': ServiceFact,
		'Benefits':Sub_benifit,
		'serviceweoffer':[Sub_serviceWeOffer,randint(0, 1)],
		'devLifecycle':DevLifecycle,
		'engagement':Engagement,
		'middleimage':Middleimage,
		'bottomdiv':Bottomdiv,
		'cat':cats
		}
	return render(request, 'service/subservice.html',res)