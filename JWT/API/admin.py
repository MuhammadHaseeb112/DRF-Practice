from django.contrib import admin
from API.models import Student,Teacher
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['id','name','roll','city']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display =['id','name','register','Subject']