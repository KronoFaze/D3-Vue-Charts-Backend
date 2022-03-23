from django.contrib import admin

from .models import Dummy, Student, Sales

admin.site.register(Dummy)
admin.site.register(Student)
admin.site.register(Sales)
