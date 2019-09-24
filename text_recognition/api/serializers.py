from rest_framework import serializers
from .models import*


class AadharSerializer(serializers.ModelSerializer):

    class Meta:

        model = Aadhar

        fields = ('id','url','name','address_aadhar_no')



