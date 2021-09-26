from service.models import service
from ourwork.models import Work, ourwork_cat,headbanner
from .serializers import WorkSerializers, ourwork_catSerializer,headbannerSerializers, serviceSerializers
from rest_framework import viewsets,filters
from . import serviceSerializer
from service import models as serviceModel
#modelviewset
# class studentModelViewset(viewsets.ModelViewSet):
#     queryset = student.objects.all()
#     serializer_class = studentSerializer

# read only model view set you can only read update and retrieve method is not working
class ourWork_catModelViewset(viewsets.ModelViewSet):
    queryset = ourwork_cat.objects.all()
    serializer_class = ourwork_catSerializer
class headbannerModelViewset(viewsets.ModelViewSet):
    queryset = headbanner.objects.all()
    serializer_class = headbannerSerializers
    filterset_fields = ('id','catagory__slug', )
class ourworkModelViewset(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    filterset_fields = ('id','catagory__slug', )
class ourServiceModelViewset(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = serviceSerializers
    filterset_fields = ('id', )

class ServiceHeadbannerModelViewset(viewsets.ModelViewSet):
    queryset = serviceModel.headbanner.objects.all()
    serializer_class = serviceSerializer.headbannerSerializers
    filterset_fields = ('id','service','sub_service','service__slug','sub_service__slug' )
class subServiceModelViewset(viewsets.ModelViewSet):
    queryset = serviceModel.subservices.objects.all()
    serializer_class = serviceSerializer.subserviesSerializers
    filterset_fields = ('id','service__slug','sub_service__slug' )
class serviceSubMenuModelViewset(viewsets.ModelViewSet):
    queryset = serviceModel.ServiceSubMenu.objects.all()
    serializer_class = serviceSerializer.serviesSubMenuSerializers
    filterset_fields = ('id','service__slug', )
