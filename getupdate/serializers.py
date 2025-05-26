from rest_framework import serializers
from getupdate.models import GetMailModel

class GetMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetMailModel
        fields = ['id', 'mail', 'created_at']
        read_only_fields = ['created_at']

    def validate_mail(self, value):
        if GetMailModel.objects.filter(mail = value).exists():
            raise serializers.ValidationError("This email is already exists.")
        return value
