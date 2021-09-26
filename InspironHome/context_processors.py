from service.models import service,ServiceSubMenu,subservices,sub_serviceWeOffer
from .models import ourwork
from ourwork.models import ourwork_cat
def alltimefunc(request):
    services = service.objects.values('id','title')
    work = ourwork_cat.objects.values('title')
    for ser in services:
        sObject = service.objects.get(id = ser['id'])
        dropdown = ServiceSubMenu.objects.filter(service=sObject)
        if len(dropdown)>0:
            ser.update({'dropdown':dropdown})
    dic1 = []
    dic2 = []
    for item in services:
        try:
            a= item['dropdown']
            dic1.append(item)
        except Exception as e:
            dic2.append(item)
    dic1.extend(dic2)
    services= dic1
    responce= {
       'services':services,
       'ourwork':work
    }
    return responce