from .models import ourwork_cat,headbanner
from .serializers import ourwork_catSerializer,headbannerSerializers
from rest_framework import viewsets,filters
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
    filterset_fields = ('id','catagory', )