from django.contrib import admin
from polls.models import Room

class RoomInline(admin.TabularInline):
	model = Room
	extra = 3

admin.site.register(Room)
