from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def Home(request):
    return render(request, 'index.html')

def Form(request):
    if request.method == 'POST':
        Complain_id = request.POST.get('Complain_id')
        Name = request.POST.get('Name')
        Assigned_Date = request.POST.get('Assigned_Date')
        Completed_Date = request.POST.get('Completed_Date')
        Description = request.POST.get('Description')
        Status = request.POST.get('Status')
        if not Completed_Date:
            Completed_Date = None
        myform = models.complaint(Complain_id=Complain_id, Name=Name, Assigned_Date=Assigned_Date, Completed_Date=Completed_Date, Description=Description, Status=Status)
        myform.save()
        return HttpResponseRedirect("complain")
    else:
        form = models.ComplaintForm
        return render(request, 'form.html', {'form': form, 'page_title': 'Complain Form'})

def ReportView(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        status = request.POST.get('Status')
        if not from_date and not to_date:
            if status == 'All':
                data = models.complaint.objects.all()
            else:
                data = models.complaint.objects.filter(Status = status)
        elif not to_date:
            if status == 'All':
                data = models.complaint.objects.filter(Assigned_Date__gte = from_date)
            else:
                data = models.complaint.objects.filter(Assigned_Date__gte = from_date,Status = status)
        elif not from_date:
            if status == 'All':
                data = models.complaint.objects.filter(Assigned_Date__lte = to_date)
            else:
                data = models.complaint.objects.filter(Assigned_Date__lte = to_date, Status = status)
        else:
            if status == 'All':
                data = models.complaint.objects.filter(Assigned_Date__gte = from_date, Assigned_Date__lte = to_date)
            else:
                data = models.complaint.objects.filter(Assigned_Date__gte = from_date, Assigned_Date__lte = to_date, Status = status)
        return render(request, 'report.html', {'data': data, 'page_title': 'Generated Report'})
    else:
        return render(request,'report.html', {'page_title': 'Report'})