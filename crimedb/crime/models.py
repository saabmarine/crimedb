from django.db import models
from django.forms import ModelForm

crime_choices = (('active','active'), ('solved','solved'),('deleted','deleted'))
achoices = (('active','active'),('deleted','deleted'))

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.loc_name

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.title
		
class Suspect(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    status = models.CharField(max_length=200,choices=achoices)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Agent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    status = models.CharField(max_length=200,choices=achoices)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Report(models.Model):
    category = models.ForeignKey(Category)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.ForeignKey(Location)
    status = models.CharField(max_length=200,choices=crime_choices)
    agent = models.ManyToManyField(Agent, through='Investigate', limit_choices_to={'status':'active'})
    suspect = models.ForeignKey(Suspect, null=True, on_delete=models.SET_NULL, limit_choices_to={'status':'active'})# on delete no cascade
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)

class Investigate(models.Model):
    report = models.ForeignKey(Report, null=True, on_delete=models.SET_NULL, limit_choices_to={'status':'active'})# on delete no cascade
    agent = models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL, limit_choices_to={'status':'active'})# on delete no cascade
    status = models.CharField(max_length=200,choices=achoices)
    def __str__(self):
        return str(self.pk)

##################################
#Forms
##################################
class SuspectForm(ModelForm):
    class Meta:
        model = Suspect
        fields = ['first_name', 'last_name', 'location']

class SuspectPartialForm(ModelForm):
    class Meta:
        model = Suspect
        fields = ['first_name', 'last_name']
		
class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'location']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['loc_name']
		
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['category', 'date', 'time', 'location', 'suspect', 'agent','status']
        help_texts = {
            'date': 'Format: mm/dd/yyyy',
            'time': 'Format: 24hrs',
        }