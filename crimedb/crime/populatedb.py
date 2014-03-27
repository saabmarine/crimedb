from crime.models import Category, Location, Agent, Suspect, Report, Investigate
from django.shortcuts import get_object_or_404
from datetime import date
import random

def populate_location():
	print("Populating 'Location'...")
	#25
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
	Location(loc_name='Bacoor').save()
	print('Bacoor inserted...')
	Location(loc_name='Cavite').save()
	print('Cavite inserted...')

	print("Done populating 'Location'")
	return

def populate_category():
	print("Populating 'Category'...")
	#10
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
	Category(title='Piracy').save()
	print('Piracy inserted...')
	Category(title='Racketeering').save()
	print('Racketeering inserted...')

	print("Done populating 'Category'")
	return

def populate_agent():
	print("Populating 'Agent'...")
	#50

	first = ['Kevin','Anthony','Kevin','Chris','Stephen','Dirk','James','Serge','Lamarcus','Russel',
			'Damian','Isaiah','Goran','Ty','Rudy','Demarcus','DeAndre','Mike','Blake','Chandler',
			'Kevin','Tim','Marc','Andrew','Eric','Ricky','Wesley','Klay','Pau','Jose',
			'Jrue', 'Gerald', 'JJ', 'Gordan', 'Monta', 'David', 'Jamal','Channing', 'Shawn', 'Derrick',
			'Manu', 'Patrick', 'Danny', 'Andrei', 'Terrence', 'Mo', 'Wilson', 'Darren', 'Kenneth', 'Eric']

	last = ['Durant','Davis','Love','Paul','Curry','Nowitzki','Harden','Ibaka','Aldridge','Westbrook',
			'Lillard','Thomas','Dragic','Lawson','Gay','Cousins','Jordan','Conley','Griffin','Parsons',
			'Martin', 'Duncan', 'Gasol', 'Bogut', 'Bledsoe', 'Rubio', 'Mathhews', 'Thompson', 'Gasol', 'Calderon',
			'Holiday', 'Green', 'Redick', 'Hayward', 'Ellis', 'Lee', 'Crawford', 'Frye', 'Marion','Favors',
			'Ginobli', 'Beverly', 'Green', 'Iguodala', 'Jones', 'Williams', 'Chandler', 'Collison','Faried', 'Gordon']

	for i in range(0,50):
		Agent(first_name=first[i],last_name=last[i],status="active",location=(get_object_or_404(Location,pk=(random.randint(1,25))))).save()
		print(str(first[i])+' '+str(last[i])+' inserted...' + str(i))

	print("Done populating 'Agent'")	
	return

def populate_suspect():
	print("Populating 'Suspect'...")
	#50

	first = ['Lebron','Carmelo','Paul','Kyle','Brook','Trevor','Paul','Al','Chris','John',
			'Kyrie','Joakim','Kyle','Andre','Thaddeus','Spencer','Dwyane','Demar','Kemba','David',
			'Marcin','Jimmy', 'Deron','Aaron','Tyson','Anderson', 'Paul','George', 'Amir','Roy',
			'Brandon','Luol','Tobias','Bradley','Greg','Lance','Joe','Brandon', 'Jameer','Mike',
			'Josh','John','Victor','Andrea','DJ','Jeff','Michael','Patrick','JR','Jeff']

	last = ['James','Anthony','George','Lowry','Lopez','Ariza','Millsap','Jefferson','Bosh','Wall',
			'Irving','Noah', 'Korver','Drummond','Young','Hawes','Wade','Derozan','Walker','West',
			'Gortat','Butler','Williams','Afflalo','Chandler','Varejao','Pierce','Hill','Johnson','Hibbert',
			'Jennings','Deng','Harris','Beal','Monroe','Stephenson','Johnson','Knight','Nelson','Dunleavy',
			'Smith','Henson','Oladipo','Bargnani','Agustin','Green','Carter-Williams','Patterson','Smith','Teague']

	for i in range(0,50):
		Suspect(first_name=first[i],last_name=last[i],status="active",location=(get_object_or_404(Location,pk=(random.randint(1,25))))).save()
		print(str(first[i])+' '+str(last[i])+' inserted...' + str(i))

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
		Report(location=(get_object_or_404(Location,pk=(random.randint(1,25)))),category=(get_object_or_404(Category,pk=(random.randint(1,10)))),suspect=(get_object_or_404(Suspect,pk=(random.randint(1,50)))),status="active", time=random_time,date=random_day).save()
		print('Report #'+str(n)+' inserted...')

	print("Done populating 'Report'")
	return

def populate_investigate(n):
	print("Populating 'Investigate'...")
#	count = 0
	nn = int(n)+1
	for a in range(1,nn):
		x = random.randint(2,11)
		for b in range(1,x):
			t = random.randint(1,50)
			if Investigate.objects.all().filter(report=(get_object_or_404(Report,pk=a)),agent=(get_object_or_404(Agent,pk=t)),status="active").exists()==False:
				Investigate(report=(get_object_or_404(Report,pk=a)),agent=(get_object_or_404(Agent,pk=t)),status="active").save()
				print('Investigate #'+str(a)+'.'+str(b)+' inserted...')		

	print("Done populating 'Investigate'")
	return

def populate():
	n = input('Enter number of reports ( greater than 100 ): ')
	print('Start populating database...')
	populate_location()
	populate_category()
	populate_agent()
	populate_suspect()
	populate_report(n)
	populate_investigate(n)
	print('Database populated')
	return