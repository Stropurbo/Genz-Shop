from rest_framework import viewsets, filters
from getupdate.serializers import GetMailSerializer
from getupdate.models import GetMailModel

class MailViewSet(viewsets.ModelViewSet):
    serializer_class = GetMailSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['mail']
    ordering_fields = ['id', 'mail']

    def get_queryset(self):
        return GetMailModel.objects.all()
    

