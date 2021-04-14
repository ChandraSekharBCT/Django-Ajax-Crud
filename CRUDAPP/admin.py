from django.contrib import admin
from .models import StudentData
# Register your models here.
class StudentDataAdmin(admin.ModelAdmin):
	list_display=['id','name','email','gender','created_at']
admin.site.register(StudentData,StudentDataAdmin)