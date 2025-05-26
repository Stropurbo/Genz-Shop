from rest_framework import viewsets
from getupdate.serializers import GetMailSerializer
from getupdate.models import GetMailModel

class MailViewSet(viewsets.ModelViewSet):
    serializer_class = GetMailSerializer
    queryset = GetMailModel.objects.all()

