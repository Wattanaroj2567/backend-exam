from django_filters import FilterSet, filters

from .models import Classroom, School, Student, Teacher


class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = School
        fields = ("name",)


class ClassroomFilter(FilterSet):
    class Meta:
        model = Classroom
        fields = ("school",)


class PersonnelFilter(FilterSet):
    firstname = filters.CharFilter(field_name="first_name", lookup_expr="icontains")
    lastname = filters.CharFilter(field_name="last_name", lookup_expr="icontains")
    gender = filters.CharFilter(lookup_expr="iexact")


class TeacherFilter(PersonnelFilter):
    school = filters.NumberFilter(field_name="classrooms__school_id", distinct=True)
    classroom = filters.NumberFilter(field_name="classrooms__id", distinct=True)

    class Meta:
        model = Teacher
        fields = ("school", "classroom", "firstname", "lastname", "gender")


class StudentFilter(PersonnelFilter):
    school = filters.NumberFilter(field_name="classroom__school_id")
    classroom = filters.NumberFilter(field_name="classroom_id")

    class Meta:
        model = Student
        fields = ("school", "classroom", "firstname", "lastname", "gender")
