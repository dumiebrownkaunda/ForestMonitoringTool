from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from FMT.api.serializers import ImageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = ImageSerializer
