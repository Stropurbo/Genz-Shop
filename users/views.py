from requests import Response
from rest_framework import viewsets, permissions, status
from django.contrib.auth import get_user_model
from users.serializers import CurrentUserSerializers

User = get_user_model()

class AdminUserViewSet(viewsets.ModelViewSet):
    serializer_class = CurrentUserSerializers
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status = status.HTTP_204_NO_CONTENT)
