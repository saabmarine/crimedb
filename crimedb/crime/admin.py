from django.contrib import admin

# Register your models here.
from crime.models import Location
from crime.models import Category
from crime.models import Agent
from crime.models import Suspect
from crime.models import Investigate
from crime.models import Report

class LocationAdmin(admin.ModelAdmin):
	list_display = ('id','loc_name')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id','title')

class SuspectAdmin(admin.ModelAdmin):
	list_display = ('id','first_name','last_name','location','status')

class AgentAdmin(admin.ModelAdmin):
	list_display = ('id','first_name','last_name','location','status')

class ReportAdmin(admin.ModelAdmin):
	list_display = ('id','date','time','category','location','suspect','status')

class InvestigateAdmin(admin.ModelAdmin):
	list_display = ('id','report','agent')

admin.site.register(Location,LocationAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Suspect,SuspectAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Report,ReportAdmin)
admin.site.register(Investigate,InvestigateAdmin)