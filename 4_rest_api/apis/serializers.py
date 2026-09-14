from rest_framework import serializers

from .models import Classroom, School, Student, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ("id", "name", "abbreviation", "address")


class SchoolDetailSerializer(SchoolSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + (
            "classroom_count",
            "teacher_count",
            "student_count",
        )


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ("id", "school", "year_level", "room_number")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "first_name", "last_name", "gender", "classrooms")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "gender", "classroom")


class ClassroomDetailSerializer(ClassroomSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta(ClassroomSerializer.Meta):
        fields = ClassroomSerializer.Meta.fields + ("teachers", "students")


class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassroomSerializer(many=True, read_only=True)


class StudentDetailSerializer(StudentSerializer):
    classroom = ClassroomSerializer(read_only=True)
