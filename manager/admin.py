from django.contrib import admin
from django.contrib.auth.models import User

from.models import Assignments, Categories
# Register your models here.

admin.site.register(Categories)
admin.site.register(Assignments)