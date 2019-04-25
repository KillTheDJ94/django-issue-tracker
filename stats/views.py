from django.shortcuts import render, HttpResponse
import pygal
from bugs.models import Bugs
from features.models import Features

def stats(request):
    a_chart = pygal.Pie()
    a_chart.title = "All Bug Reports"
    a_chart.add("To Do", Bugs.objects.filter(development_status="To Do").count() + Features.objects.filter(development_status="To Do").count())
    a_chart.add("Currently Being Investigated", Bugs.objects.filter(development_status="Currently Being Investigated").count() + Features.objects.filter(development_status="Currently Being Investigated").count())
    a_chart.add("In Development", Bugs.objects.filter(development_status="In Development").count() + Features.objects.filter(development_status="In Development").count())
    a_chart.add("In Testing", Bugs.objects.filter(development_status="In Testing").count() + Features.objects.filter(development_status="In Testing").count())
    chart1 = a_chart.render_data_uri()
    
    b_chart = pygal.Bar()
    b_chart.title = "Bug Reports"
    b_chart.add("To Do", Bugs.objects.filter(development_status="To Do", tag="Bug").count())
    b_chart.add("Currently Being Investigated", Bugs.objects.filter(development_status="Currently Being Investigated", tag="Bug").count())
    b_chart.add("In Development", Bugs.objects.filter(development_status="In Development", tag="Bug").count())
    b_chart.add("In Testing", Bugs.objects.filter(development_status="In Testing", tag="Bug").count())
    chart2 = b_chart.render_data_uri()
    
    c_chart = pygal.Bar()
    c_chart.title = "Feature Reports"
    c_chart.add("To Do", Features.objects.filter(development_status="To Do", tag="Feature Request").count())
    c_chart.add("Currently Being Investigated", Features.objects.filter(development_status="Currently Being Investigated", tag="Feature Request").count())
    c_chart.add("In Development", Features.objects.filter(development_status="In Development", tag="Feature Request").count())
    c_chart.add("In Testing", Features.objects.filter(development_status="In Testing",tag="Feature Request").count())
    chart3 = c_chart.render_data_uri()
    
    return render(request, 'development_status_stats.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3})