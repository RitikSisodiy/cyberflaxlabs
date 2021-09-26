from service.models import headbanner,subservices,ServiceSubMenu
from rest_framework import serializers

class headbannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = headbanner
        fields = '__all__'
class serviesSubMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceSubMenu
        fields = '__all__'
class subserviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = subservices
        fields = '__all__'