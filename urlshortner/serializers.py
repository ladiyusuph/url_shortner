import random
import string
from rest_framework import serializers
from .models import UrlShortner


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortner
        fields = "__all__"

    # def validate(self, data):
    #     if not data.get("slug"):
    #         data["slug"] = "".join(
    #             random.choices(string.ascii_letters + string.digits, k=10)
    #         )
    #     return data

    # def create(self, validated_data):
    #     return UrlShortner.objects.create(**validated_data)
