from django.db import models
from rest_framework import serializers
from . models import ourwork_cat,headbanner
class ourwork_catSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourwork_cat
        fields = ['id','title','slug']
class headbannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = headbanner
        fields = '__all__'