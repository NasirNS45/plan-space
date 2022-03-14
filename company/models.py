from django.db import models


class Contact(models.Model):
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.phone_number)


class Space(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Location(models.Model):
    location = models.CharField(max_length=255, null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to="locations", null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    only_virtual_location = models.BooleanField(default=False, null=True, blank=True)
    only_physical_location = models.BooleanField(default=False, null=True, blank=True)
    only_mailing_address = models.BooleanField(default=False, null=True, blank=True)
    contacts = models.ManyToManyField(Contact, blank=True)
    spaces = models.ManyToManyField(Space, blank=True)

    def __str__(self):
        return str(self.location)
