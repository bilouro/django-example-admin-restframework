from .models import *
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'number')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'address', 'contacts']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']
