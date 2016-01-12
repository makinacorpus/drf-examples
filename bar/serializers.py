from rest_framework import serializers

from .models import Bar


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
