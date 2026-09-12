from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Изменять и удалять объявление может только его автор."""

    def has_object_permission(self, request, view, obj):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return obj.creator == request.user