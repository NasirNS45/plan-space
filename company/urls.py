from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register("location", views.LocationViewSet)
router.register("space", views.SpaceViewSet)
router.register("contact", views.ContactViewSet)

urlpatterns = [path("", include(router.urls))]
