from django.contrib import admin
from .models import MyUsers, Albums, Tracks


@admin.register(MyUsers, Albums, Tracks)
class MyUsersAdmin(admin.ModelAdmin):
    pass
