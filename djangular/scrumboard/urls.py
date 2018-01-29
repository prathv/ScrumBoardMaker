from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .api import ListViewSet, CardViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'lists',ListViewSet)
router.register(r'cards',CardViewSet)

urlpatterns = router.urls
