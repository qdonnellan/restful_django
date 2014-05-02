from rest_framework import routers
from restful_api.views import ThingViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'things', ThingViewSet)
