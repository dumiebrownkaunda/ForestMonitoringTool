from .models import user
from rest_framework import serializers


class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
#        fields = ('firstname', 'lastname',)

    fields = '__all__'
