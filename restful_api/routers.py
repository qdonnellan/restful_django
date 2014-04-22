from rest_framework import routers
from restful_api.views import ThingViewSet

router = routers.DefaultRouter()
router.register(r'things', ThingViewSet)