from django.contrib import admin
from main.models import ToDo
# Register your models here.


class Todo(admin.ModelAdmin):
    list_display = ("title", "discription", "sent_at")



admin.site.register(ToDo)
