from rest_framework import filters


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    Returns all objects for staff.
    """
    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(user=user) if not user.is_staff else queryset
