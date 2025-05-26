from rest_framework import viewsets, mixins
from getupdate.serializers import GetMailSerializer
from getupdate.models import GetMailModel

class MailViewSet(mixins.CreateModelMixin,
    viewsets.ModelViewSet):
    serializer_class = GetMailSerializer
    queryset = GetMailModel.objects.all()

