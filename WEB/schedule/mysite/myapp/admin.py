from django.contrib import admin
from .models import Teacher, Student, Subject


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic_name', 'login', 'password')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group_num', 'student_number', 'login', 'course')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('day', 'subject', 'number_of_class', 'classroom', 'group_num', 'teacher', 'subgroup')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
