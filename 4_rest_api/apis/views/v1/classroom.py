from rest_framework.viewsets import ModelViewSet

from apis.filters import ClassroomFilter
from apis.models import Classroom
from apis.serializers import ClassroomDetailSerializer, ClassroomSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.order_by("id")
    serializer_class = ClassroomSerializer
    filterset_class = ClassroomFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "retrieve":
            return queryset.prefetch_related("teachers__classrooms", "students")
        return queryset

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ClassroomDetailSerializer
        return super().get_serializer_class()
