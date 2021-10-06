from rest_framework import serializers
from test_data.models import TestData


class TestDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "description", "date")
        model = TestData