from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from common.filters import IsOwnerFilterBackend
from common.permissions import IsOwner


class BaseUserOwnedModelViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()` and automatically adds an
    authenticated user as the model's owner.
    """
    permission_classes = (IsAuthenticated, IsOwner)
    filter_backends = (IsOwnerFilterBackend,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
