from rest_framework import serializers
from . import models


class LocationSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    spaces = serializers.SerializerMethodField()

    class Meta:
        model = models.Location
        fields = [
            "id",
            "location",
            "address_line_1",
            "address_line_2",
            "city",
            "state",
            "zip_code",
            "image",
            "only_virtual_location",
            "only_physical_location",
            "only_mailing_address",
            "contacts",
            "spaces",
        ]

    def get_spaces(self, obj):
        if obj.spaces:
            return [space.name for space in obj.spaces.all()]
        return []

    def get_contacts(self, obj):
        if obj.contacts:
            return [
                {"phone_number": contact.phone_number, "email": contact.email}
                for contact in obj.contacts.all()
            ]
        return []


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Space
        fields = "__all__"
