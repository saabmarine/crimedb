from crime.models import Category, Location, Agent, Suspect, Report, Investigate
from django.shortcuts import get_object_or_404
from datetime import date
import random

def populate_location():
	print("Populating 'Location'...")
	#23
	Location(loc_name='Manila').save()
	print('Manila inserted...')
	Location(loc_name='Caloocan').save()
	print('Caloocan inserted...')
	Location(loc_name='Las Pinas').save()
	print('Las Pinas inserted...')
	Location(loc_name='Makati').save()
	print('Makati inserted...')
	Location(loc_name='Malabon').save()
	print('Malabon inserted...')
	Location(loc_name='Mandaluyong').save()
	print('Mandaluyong inserted...')
	Location(loc_name='Marikina').save()
	print('Marikina inserted...')
	Location(loc_name='Muntinlupa').save()
	print('Muntinlupa inserted...')
	Location(loc_name='Navotas').save()
	print('Navotas inserted...')
	Location(loc_name='Paranaque').save()
	print('Paranaque inserted...')
	Location(loc_name='Pasay').save()
	print('Pasay inserted...')
	Location(loc_name='Pasig').save()
	print('Pasig inserted...')
	Location(loc_name='Quezon City').save()
	print('Quezon City inserted...')
	Location(loc_name='San Juan').save()
	print('San Juan inserted...')
	Location(loc_name='Taguig').save()
	print('Taguig inserted...')
	Location(loc_name='Valenzuela').save()
	print('Valenzuela inserted...')
	Location(loc_name='Pateros').save()
	print('Pateros inserted...')
	Location(loc_name='Antipolo').save()
	print('Antipolo inserted...')
	Location(loc_name='Batangas').save()
	print('Batangas inserted...')
	Location(loc_name='Lipa').save()
	print('Lipa inserted...')
	Location(loc_name='Malolos').save()
	print('Maloloas inserted...')
	Location(loc_name='Calamba').save()
	print('Calamba inserted...')
	Location(loc_name='Santa Rosa').save()
	print('Santa Rosa inserted...')

	print("Done populating 'Location'")
	return

def populate_category():
	print("Populating 'Category'...")
	#8
	Category(title='Murder').save()
	print('Murder inserted...')
	Category(title='Robbery').save()
	print('Robbery inserted...')
	Category(title='Assault').save()
	print('Assault inserted...')
	Category(title='Kidnapping').save()
	print('Kidnapping inserted...')
	Category(title='Extortion').save()
	print('Extortion inserted...')
	Category(title='Theft').save()
	print('Theft inserted...')
	Category(title='Smuggling').save()
	print('Smuggling inserted...')
	Category(title='Vandalism').save()
	print('Vandalism inserted...')

	print("Done populating 'Category'")
	return

def populate_agent():
	print("Populating 'Agent'...")
	#20
	Agent(first_name="Kevin",last_name="Durant",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kevin Durant inserted...')
	Agent(first_name="Anthony",last_name="Davis",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Anthony Davis inserted...')
	Agent(first_name="Kevin",last_name="Love",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kevin Love inserted...')
	Agent(first_name="Chris",last_name="Paul",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Chris Paul inserted...')
	Agent(first_name="Stephen",last_name="Curry",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Stephen Curry inserted...')
	Agent(first_name="Dirk",last_name="Nowitzki",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Dirk Nowitzki inserted...')
	Agent(first_name="James",last_name="Harden",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('James Harden inserted...')
	Agent(first_name="Serge",last_name="Ibaka",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Serge Ibaka inserted...')
	Agent(first_name="Lamarcus",last_name="Aldridge",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Lamarcus Aldridge inserted...')
	Agent(first_name="Russel",last_name="Westbrook",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Russel Westbrook inserted...')
	Agent(first_name="Damian",last_name="Lillard",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Damian Lillard inserted...')
	Agent(first_name="Isaiah",last_name="Thomas",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Isaiah Thomas inserted...')
	Agent(first_name="Goran",last_name="Dragic",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Goran Dragic inserted...')
	Agent(first_name="Ty",last_name="Lawson",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Ty Lawson inserted...')
	Agent(first_name="Rudy",last_name="Gay",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Rudy Gay inserted...')
	Agent(first_name="Demarcus",last_name="Cousins",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Demarcus Cousins inserted...')
	Agent(first_name="DeAndre",last_name="Jordan",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('DeAndre Jordan inserted...')
	Agent(first_name="Mike",last_name="Conley",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Mike Conley inserted...')
	Agent(first_name="Blake",last_name="Griffin",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Blake Griffin inserted...')
	Agent(first_name="Chandler",last_name="Parsons",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Chandler Parsons inserted...')

	print("Done populating 'Agent'")	
	return

def populate_suspect():
	print("Populating 'Suspect'...")
	#20
	Suspect(first_name="Lebron",last_name="James",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Lebron James inserted...')
	Suspect(first_name="Carmelo",last_name="Anthony",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Carmelo Anthony inserted...')
	Suspect(first_name="Paul",last_name="George",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Paul George inserted...')
	Suspect(first_name="Kyle",last_name="Lowry",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kyle Lowry inserted...')
	Suspect(first_name="Brook",last_name="Lopez",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Brook Lopez inserted...')
	Suspect(first_name="Trevor",last_name="Ariza",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Trevor Ariza inserted...')
	Suspect(first_name="Paul",last_name="Millsap",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Paul Millsap inserted...')
	Suspect(first_name="Al",last_name="Jefferson",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Al Jefferson inserted...')
	Suspect(first_name="Chris",last_name="Bosh",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Chris Bosh inserted...')
	Suspect(first_name="John",last_name="Wall",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('John Wall inserted...')
	Suspect(first_name="Kyrie",last_name="Irving",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kyrie Irving inserted...')
	Suspect(first_name="Joakim",last_name="Noah",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Isaiah Thomas inserted...')
	Suspect(first_name="Kyle",last_name="Korver",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kyle Korver inserted...')
	Suspect(first_name="Andre",last_name="Drummond",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Andre Drummond inserted...')
	Suspect(first_name="Thaddeus",last_name="Young",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Thaddeus Young inserted...')
	Suspect(first_name="Spencer",last_name="Hawes",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Spencer Hawes inserted...')
	Suspect(first_name="Dwyane",last_name="Wade",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Dwyane Wade inserted...')
	Suspect(first_name="Demar",last_name="Derozan",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Demar Derozan inserted...')
	Suspect(first_name="Kemba",last_name="Walker",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('Kemba Walker inserted...')
	Suspect(first_name="David",last_name="West",status="active",location=(get_object_or_404(Location,pk=(random.randint(1,23))))).save()
	print('David West inserted...')

	print("Done populating 'Suspect'")	
	return

def populate_report(n):
	print("Populating 'Report'...")
	#100 reports
	#2013-1-1 up to data.today() random date of report
	#random time
	nn = int(n)+1
	for n in range(1,nn):
		start_date = date.today().replace(year=2013,month=1,day=1).toordinal()
		end_date = date.today().toordinal()
		random_day = date.fromordinal(random.randint(start_date,end_date))
		random_time = str(random.randint(00,23))+":"+str(random.randint(00,59))
		Report(location=(get_object_or_404(Location,pk=(random.randint(1,23)))),category=(get_object_or_404(Category,pk=(random.randint(1,8)))),suspect=(get_object_or_404(Suspect,pk=(random.randint(1,20)))),status="active", time=random_time,date=random_day).save()
		print('Report #'+str(n)+' inserted...')

	print("Done populating 'Report'")
	return

def populate_investigate(n):
	print("Populating 'Investigate'...")
#	count = 0
	nn = int(n)+1
	for a in range(1,nn):
		x = random.randint(2,6)
		for b in range(1,x):
			Investigate(report=(get_object_or_404(Report,pk=a)),agent=(get_object_or_404(Agent,pk=(random.randint(1,20)))),status="active").save()
			print('Investigate #'+str(a)+'.'+str(b)+' inserted...')		

	print("Done populating 'Investigate'")
	return

def populate():
	n = input('Enter number of reports (n>300): ')
	print('Start populating database...')
	populate_location()
	populate_category()
	populate_agent()
	populate_suspect()
	populate_report(n)
	populate_investigate(n)
	print('Database populated')
	return