from django.contrib import admin
from models import Student, Teacher, Class, Subject, InscriptionDetail, Evaluation, File


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(InscriptionDetail)
admin.site.register(Evaluation)
admin.site.register(File)