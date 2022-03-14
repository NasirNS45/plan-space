import json
from rest_framework import viewsets, parsers
from rest_framework.response import Response
from . import models
from . import serializers


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    queryset = models.Location.objects.all()
    parser_classes = [parsers.MultiPartParser]

    def create(self, request, *args, **kwargs):
        try:
            contacts = request.data.get("contacts")
            spaces = request.data.get("spaces")
            print(request.data.get("image"))
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            location = serializer.save()
            contact_ids = []
            if contacts:
                for contact in json.loads(contacts):
                    c = models.Contact.objects.create(
                        phone_number=int(contact["phone_number"]),
                        email=contact["email"],
                    )
                    contact_ids.append(c.pk)
                location.contacts.set(contact_ids)
            print("contacts:: ", json.loads(contacts))
            print("spaces:: ", json.loads(spaces))
            if spaces:
                location.spaces.set(json.loads(spaces))
            return Response(
                {"message": "Location added", "data": serializer.data}, status=201
            )
        except Exception as error:
            return Response({"message": str(error)}, status=400)


class SpaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SpaceSerializer
    queryset = models.Space.objects.all()
