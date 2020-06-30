from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import ReportCreateForm, ReportUpdateForm
from django.views.generic import ListView
from .models import Report
from django.contrib.auth.decorators import login_required

def report_listview(request):
    queryset = Report.objects.all();
    context = {
        "object_list":queryset
    }
    return render(request,"report/report_list.html",context)

#@login_required
# Create your views here.
def report_create_view(request, *args, **kwargs):
    form = ReportCreateForm(request.POST or None);
    if form.is_valid():
        form.save();
        form = ReportCreateForm();
    context = {
        "form":form
    }
    return render(request, "report/report_create.html", context)

def report_updateview(request, id):
    my_report = get_object_or_404(Report, id=id);
    
    #my_report = Report.objects.get(id=14)
    form = ReportUpdateForm(request.POST or None, instance=my_report)
    if form.is_valid():
        form.save();
        form = ReportUpdateForm(instance=my_report);
    context = {
        "form":form
    }
    return render(request, "report/report_update.html", context)

def report_detailview(request, id):
    my_report = get_object_or_404(Report, id=id);

    context = {
        "report":my_report
    }
    return render(request, "report/report_detail.html", context)



    