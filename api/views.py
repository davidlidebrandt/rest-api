
from rest_framework import viewsets
from rest_framework import permissions
from test_data.models import TestData
from .serializers import TestDataSerializer
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class TestDataViewSet(viewsets.ModelViewSet):
    serializer_class = TestDataSerializer
    permission_classes = (IsOwner,)
    
    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return TestData.objects.filter(creator=user)
        raise PermissionDenied()
        
    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
