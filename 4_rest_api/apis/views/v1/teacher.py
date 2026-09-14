from rest_framework.viewsets import ModelViewSet

from apis.filters import TeacherFilter
from apis.models import Teacher
from apis.serializers import TeacherDetailSerializer, TeacherSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.prefetch_related("classrooms").order_by("id")
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TeacherDetailSerializer
        return super().get_serializer_class()
