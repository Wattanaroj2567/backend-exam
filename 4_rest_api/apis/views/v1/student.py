from rest_framework.viewsets import ModelViewSet

from apis.filters import StudentFilter
from apis.models import Student
from apis.serializers import StudentDetailSerializer, StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("classroom").order_by("id")
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StudentDetailSerializer
        return super().get_serializer_class()
