from django.contrib import admin

# Register your models here.
from teacherportal.models import *


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Subjects)

"""class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'phone_number', 'room_number')


class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'subject') 
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(Subject) """
