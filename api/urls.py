from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TestDataViewSet

router = SimpleRouter()
router.register('test_data', TestDataViewSet, basename="test_data")
urlpatterns = router.urls