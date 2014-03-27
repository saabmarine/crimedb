from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from crime.models import Category, Location, Agent, Suspect, Report, Investigate
from crime.models import SuspectForm, SuspectPartialForm, ReportForm, CategoryForm, AgentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, 'index.html')

def report_crime(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            suspect = form.cleaned_data['suspect']
            agent = form.cleaned_data['agent']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            location = form.cleaned_data['location']
            category = form.cleaned_data['category']
            status = "active"
            r = Report.objects.create(location=location,date=date,time=time,category=category,suspect=suspect,status=status)
            for a in agent:
                investigate = Investigate(report=r,agent=a,status=status)
                investigate.save()
            message = "Crime successfully reported."
            return render(request, 'message.html', {"message":message})
    else:
        form = ReportForm()
    return render(request, 'report_crime.html', {'form':form,})

def crimes(request):
    reports = Report.objects.all().exclude(status='deleted')
#    paginator = Paginator(report_list,5,allow_empty_first_page=True)
#    page = request.GET.get('page')
#    try:
#        reports = paginator.page(page)
#    except PageNotAnInteger:
#        reports = paginator.page(1)
#    except EmptyPage:
#        reports = paginator.page(paginator.num_pages)
    return render(request, 'crimes.html', {"reports":reports})

def crimes_detail(request, report_id):
    crimes_detail = get_object_or_404(Report, pk=report_id)
    investigate_detail = Investigate.objects.all().filter(report=report_id).exclude(status="deleted")
#    paginator = Paginator(invetigate_detail,5,allow_empty_first_page=True)
#    page = request.GET.get('page')
#    try:
#        invetigate_detail = paginator.page(page)
#    except PageNotAnInteger:
#        invetigate_detail = paginator.page(1)
#    except EmptyPage:
#        invetigate_detail = paginator.page(paginator.num_pages)    
    return render(request, 'crimes_detail.html', {'crimes_detail':crimes_detail,'investigate_detail':investigate_detail})

def crimes_delete(request, report_id):
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=report_id)
        report.status='deleted'
        report.save()
        investigate = Investigate.objects.all().filter(report=report_id)
        for a in investigate:
            a.status='deleted'
            a.save()
            message = "Crime successfully deleted"
            return render(request, 'message.html', {"message":message})
    else:
        report = get_object_or_404(Report, pk=report_id)
    return render(request, 'crimes_delete.html', {'report':report})

def crimes_edit(request, report_id):
    old = Report.objects.get(pk=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=old)
        if form.is_valid():
            category = form.cleaned_data['category']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            location = form.cleaned_data['location']
            suspect = form.cleaned_data['suspect']
            newagents = form.cleaned_data['agent']
            old.category=category
            old.location=location
            old.suspect=suspect
            old.date=date
            old.time=time
            old.save()
            oldagents = Investigate.objects.all().filter(report=old)
            oldagents.delete()

            for d in newagents:
                investigate = Investigate(report=old,agent=d,status='active')
                investigate.save()

            message = "Crime successfully updated"
            return render(request, 'message.html', {"message":message})
    else:
        form = ReportForm(instance=old)
    return render(request, 'crimes_edit.html', {'form':form})

def homepage(request):
    timeSlotChart = ['12am', '01am','02am', '03am', '04am',
                '05am', '06am','07am', '08am', '09am',
                '10am', '11am','12pm', '01pm', '02pm',
                '03pm', '04pm','05pm', '06pm', '07pm',
                '08pm', '09pm','10pm', '11pm']
    timeSlot = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    data = []

    z = Report.objects.all().count()
    for x in range(0,24):
        if Report.objects.filter(time__startswith=timeSlot[x]).exclude(status="deleted").count() == 0:
             data.append((timeSlotChart[x],0))
        else:
            data.append((timeSlotChart[x],round(Report.objects.filter(time__startswith=timeSlot[x]).exclude(status="deleted").count()/z,2)))

    return render(request, 'homepage.html', {'data':data})

def agents(request):
    agents = Agent.objects.all().filter(status='active')
#    paginator = Paginator(agent_list,5, allow_empty_first_page=True)
#    page = request.GET.get('page')
#    try:
#        agents = paginator.page(page)
#    except PageNotAnInteger:
#        agents = paginator.page(1)
#    except EmptyPage:
#        agents = paginator.page(paginator.num_pages)
    return render(request, 'agents.html', {"agents":agents})

def agents_add(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            location = form.cleaned_data['location']
            status = "active"
            Agent(first_name=first_name, last_name=last_name,location=location, status=status).save()
            message = "Agent successfully added."
            return render(request, 'message.html', {"message":message})
    else:
	    form = AgentForm()
    return render(request, 'agents_add.html', {'form':form,})

def agents_detail(request, agent_id):
    agents_detail = get_object_or_404(Agent, pk=agent_id)
    investigating_history = Investigate.objects.all().filter(agent=agents_detail).exclude(status="deleted")
    return render(request, 'agents_detail.html', {'agents_detail':agents_detail,'investigating_history':investigating_history})

def agents_delete(request, agent_id):
    if request.method == 'POST':
        agent = get_object_or_404(Agent, pk=agent_id)
        agent.status='deleted'
       

        a = Investigate.objects.all().filter(agent=agent).exclude(status="deleted")
        for investigate in a:
            investigate.status='deleted'
            investigate.save()
        agent.save()
        message = "Agent successfully deleted"
        return render(request, 'message.html', {"message":message})
    else:
        agent = get_object_or_404(Agent, pk=agent_id)
    return render(request, 'agents_delete.html', {'agent':agent})

def agents_edit(request, agent_id):
    old = Agent.objects.get(pk=agent_id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance=old)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            location = form.cleaned_data['location']
            form.save()
            message = "Agent successfully updated"
            return render(request, 'message.html', {"message":message})
    else:
        form = AgentForm(instance=old)
    return render(request, 'agents_edit.html', {'form':form})

def suspects(request):
    suspects = Suspect.objects.all().filter(status='active')
#    paginator = Paginator(suspect_list,5, allow_empty_first_page=True)
#    page = request.GET.get('page')
#    try:
#        suspects = paginator.page(page)
#    except PageNotAnInteger:
#        suspects = paginator.page(1)
#    except EmptyPage:
#        suspects = paginator.page(paginator.num_pages)
    return render(request, 'suspects.html', {"suspects":suspects})

def suspects_add(request):
    if request.method == 'POST':
        form = SuspectForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            location = form.cleaned_data['location']
            status = "active"
            Suspect(first_name=first_name, last_name=last_name,location=location, status=status).save()
            message = "Suspect successfully added."
            return render(request, 'message.html', {"message":message})
    else:
	    form = SuspectForm()
    return render(request, 'suspects_add.html', {'form':form,})

def suspects_detail(request, suspect_id):
    suspects_detail = get_object_or_404(Suspect, pk=suspect_id)
    criminal_history = Report.objects.all().filter(suspect=suspects_detail).exclude(status="deleted")
    return render(request, 'suspects_detail.html', {'suspects_detail':suspects_detail,'criminal_history':criminal_history})

def suspects_delete(request,suspect_id):
    if request.method == 'POST':
        suspect = get_object_or_404(Suspect, pk=suspect_id)
        suspect.status='deleted'
        
        #report = get_object_or_404(Report, suspect=suspect).exclude(status="deleted")
        a = Report.objects.all().filter(suspect=suspect).exclude(status="deleted")
        for report in a:
            report.suspect=None
            report.save()
        suspect.save()
        message = "Suspect successfully deleted"
        return render(request, 'message.html', {"message":message})
    else:
        suspect = get_object_or_404(Suspect, pk=suspect_id)
    return render(request, 'suspects_delete.html', {'suspect':suspect})

def suspects_edit(request, suspect_id):
    old = Suspect.objects.get(pk=suspect_id)
    if request.method == 'POST':
        form = SuspectPartialForm(request.POST, instance=old)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            form.save()
            message = "Suspect successfully updated"
            return render(request, 'message.html', {"message":message})
    else:
        form = SuspectPartialForm(instance=old)
    return render(request, 'suspects_edit.html', {'form':form})

def locations(request):
    locations = Location.objects.all().order_by('loc_name')
    locationsChart = Location.objects.all()
#    paginator = Paginator(locations,5,allow_empty_first_page=True)
#    page = request.GET.get('page')
#    try:
#        locations = paginator.page(page)
#    except PageNotAnInteger:
#        locations = paginator.page(1)
#    except EmptyPage:
#        locations = paginator.page(paginator.num_pages)

    timeSlotChart = ['12am', '01am','02am', '03am', '04am',
                '05am', '06am','07am', '08am', '09am',
                '10am', '11am','12pm', '01pm', '02pm',
                '03pm', '04pm','05pm', '06pm', '07pm',
                '08pm', '09pm','10pm', '11pm']
    timeSlot = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    data3 = []

    z = Report.objects.all().count()
    for x in range(0,24):
        if Report.objects.filter(time__startswith=timeSlot[x]).exclude(status="deleted").count() == 0:
             data3.append((timeSlotChart[x],0))
        else:
            data3.append((timeSlotChart[x],round(Report.objects.filter(time__startswith=timeSlot[x]).exclude(status="deleted").count()/z,2)))

    categories = Category.objects.all()
    data=[]
    data2=[]
    count = Report.objects.all().exclude(status="deleted").count()
    for cat in categories:
        data.append((str(cat.title),round((((Report.objects.filter(category=cat).exclude(status="deleted").count())/count)*100),2)))
    data = sorted(data)
    x = Report.objects.all().exclude(status="deleted").count()
    for loc in locationsChart:
        if Report.objects.filter(location=loc).count() == 0:
            data2.append((str(loc.loc_name),0))
        else:
            data2.append((str(loc.loc_name),round((Report.objects.filter(location=loc).exclude(status="deleted").count()/x),2)))
    data2 = sorted(data2)
    return render(request, 'locations.html', {"locations":locations, "data":data, "data2":data2, "data3":data3,})

def locations_detail(request, loc_id):
    locations = Location.objects.all().order_by('loc_name')
    locationsChart = Location.objects.all()
    locations_detail = get_object_or_404(Location, pk=loc_id)

    timeSlotChart = ['12am', '01am','02am', '03am', '04am',
                '05am', '06am','07am', '08am', '09am',
                '10am', '11am','12pm', '01pm', '02pm',
                '03pm', '04pm','05pm', '06pm', '07pm',
                '08pm', '09pm','10pm', '11pm']
    timeSlot = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    data = []
    z = Report.objects.filter(location=locations_detail).exclude(status="deleted").count()
    for x in range(0,24):
        if Report.objects.filter(location=locations_detail).filter(time__startswith=timeSlot[x]).exclude(status="deleted").count() == 0:
             data.append((timeSlotChart[x],0))
        else:
            data.append((timeSlotChart[x],round(Report.objects.filter(location=locations_detail).filter(time__startswith=timeSlot[x]).exclude(status="deleted").count()/z,2)))

    categories = Category.objects.all()
    data2=[]
    count = Report.objects.filter(location=locations_detail).exclude(status="deleted").count()
    for cat in categories:
        c = Report.objects.filter(category=cat,location=locations_detail).exclude(status="deleted").count()
        if c == 0:
            data2.append((str(cat.title),0))
        else:
            data2.append((str(cat.title),round((((Report.objects.filter(category=cat,location=locations_detail).exclude(status="deleted").count())/count)*100),2)))
    data2 = sorted(data2)

    return render(request, 'locations_detail.html', {'locations_detail':locations_detail, 'locations':locations, 'data':data, 'data2':data2})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            Category(title=title).save()
            return HttpResponseRedirect('/crime/thanks')
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form':form,})

def search(request):
    return render(request, 'search.html')

def thanks(request):
    return HttpResponse("Thanks!")
