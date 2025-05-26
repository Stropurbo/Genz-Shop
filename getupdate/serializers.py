from rest_framework import serializers
from getupdate.models import GetMailModel

class GetMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetMailModel
        fields = ['id', 'mail']
