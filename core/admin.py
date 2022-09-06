from django.contrib import admin
from .models import (
    StudentProfile,
    TeacherProfile,
    Course,
    RegisteredCourse,
    Lecture,
    Video,
)

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Course)
admin.site.register(RegisteredCourse)
admin.site.register(Lecture)
admin.site.register(Video)
