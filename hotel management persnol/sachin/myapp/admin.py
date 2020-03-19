

from django.contrib import admin
from .models import *

admin.register(Room,Reserve)(admin.ModelAdmin)