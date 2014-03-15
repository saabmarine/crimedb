from django.contrib import admin

# Register your models here.
from crime.models import Location
from crime.models import Category
from crime.models import Agent
from crime.models import Suspect
from crime.models import Investigate
from crime.models import Report

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Suspect)
admin.site.register(Agent)
admin.site.register(Report)
admin.site.register(Investigate)