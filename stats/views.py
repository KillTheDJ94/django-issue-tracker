from django.shortcuts import render, HttpResponse
import pygal
from bugs.models import Bugs
from features.models import Features
from django.utils import timezone
import datetime
from datetime import timedelta
from pygal.style import DefaultStyle

def stats(request):
    a_chart = pygal.Pie(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    a_chart.title = "All Bug Reports"
    a_chart.add("To Do", Bugs.objects.filter(development_status="To Do").count() + Features.objects.filter(development_status="To Do").count())
    a_chart.add("Currently Being Investigated", Bugs.objects.filter(development_status="Currently Being Investigated").count() + Features.objects.filter(development_status="Currently Being Investigated").count())
    a_chart.add("In Development", Bugs.objects.filter(development_status="In Development").count() + Features.objects.filter(development_status="In Development").count())
    a_chart.add("In Testing", Bugs.objects.filter(development_status="In Testing").count() + Features.objects.filter(development_status="In Testing").count())
    chart1 = a_chart.render_data_uri()
    
    b_chart = pygal.Bar(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    b_chart.title = "Bug Reports"
    b_chart.add("To Do", Bugs.objects.filter(development_status="To Do", tag="Bug").count())
    b_chart.add("Currently Being Investigated", Bugs.objects.filter(development_status="Currently Being Investigated", tag="Bug").count())
    b_chart.add("In Development", Bugs.objects.filter(development_status="In Development", tag="Bug").count())
    b_chart.add("In Testing", Bugs.objects.filter(development_status="In Testing", tag="Bug").count())
    chart2 = b_chart.render_data_uri()
    
    c_chart = pygal.Bar(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    c_chart.title = "Feature Reports"
    c_chart.add("To Do", Features.objects.filter(development_status="To Do", tag="Feature Request").count())
    c_chart.add("Currently Being Investigated", Features.objects.filter(development_status="Currently Being Investigated", tag="Feature Request").count())
    c_chart.add("In Development", Features.objects.filter(development_status="In Development", tag="Feature Request").count())
    c_chart.add("In Testing", Features.objects.filter(development_status="In Testing",tag="Feature Request").count())
    chart3 = c_chart.render_data_uri()
    
    d_chart = pygal.Pie(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    d_chart.title = "Total Number Of Bug Reports And Feature Requests"
    d_chart.add("Bug Reports", Bugs.objects.filter(tag="Bug").count())
    d_chart.add("Feature Requests", Features.objects.filter(tag="Feature Request").count())
    chart4 = d_chart.render_data_uri()
    
    e_chart = pygal.HorizontalBar(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    e_chart.title = "Bug reports generated weekly"
    e_chart.add("Today", Bugs.objects.filter(tag="Bug", published_date=timezone.now()).count())
    e_chart.add("Yesterday", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=1)).count())
    e_chart.add("2 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=2)).count())
    e_chart.add("3 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=3)).count())
    e_chart.add("4 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=4)).count())
    e_chart.add("5 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=5)).count())
    e_chart.add("6 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=6)).count())
    e_chart.add("7 days", Bugs.objects.filter(tag="Bug",published_date=timezone.now().date() - timedelta(days=7)).count())
    chart5 = e_chart.render_data_uri()
    
    f_chart = pygal.HorizontalBar(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    f_chart.title = "Feature Requests generated weekly"
    f_chart.add("Today", Features.objects.filter(tag="Feature Request", published_date=timezone.now()).count())
    f_chart.add("Yesterday", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=1)).count())
    f_chart.add("2 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=2)).count())
    f_chart.add("3 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=3)).count())
    f_chart.add("4 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=4)).count())
    f_chart.add("5 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=5)).count())
    f_chart.add("6 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=6)).count())
    f_chart.add("7 days", Features.objects.filter(tag="Feature Request",published_date=timezone.now().date() - timedelta(days=7)).count())
    chart6 = f_chart.render_data_uri()
    
    g_chart = pygal.Pie(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    g_chart.title = "Bugs Investigated weekly"
    g_chart.add("Today", Bugs.objects.filter(tag="Bug", development_status="Currently Being Investigated", published_date=timezone.now()).count())
    g_chart.add("Yesterday", Bugs.objects.filter(tag="Bug", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=1)).count())
    g_chart.add("2 days", Bugs.objects.filter(tag="Bug", development_status="Currently Being Investigated",published_date=timezone.now().date() - timedelta(days=2)).count())
    g_chart.add("3 days", Bugs.objects.filter(tag="Bug",development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=3)).count())
    g_chart.add("4 days", Bugs.objects.filter(tag="Bug",development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=4)).count())
    g_chart.add("5 days", Bugs.objects.filter(tag="Bug",development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=5)).count())
    g_chart.add("6 days", Bugs.objects.filter(tag="Bug",development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=6)).count())
    g_chart.add("7 days", Bugs.objects.filter(tag="Bug",development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=7)).count())
    chart7 = g_chart.render_data_uri()
    
    h_chart = pygal.Pie(print_values=True, style=DefaultStyle(
                  value_font_family='helvetica',
                  value_font_size=30))
    h_chart.title = "Feature Requests Investigated weekly"
    h_chart.add("Today", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now()).count())
    h_chart.add("Yesterday", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=1)).count())
    h_chart.add("2 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=2)).count())
    h_chart.add("3 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=3)).count())
    h_chart.add("4 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=4)).count())
    h_chart.add("5 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=5)).count())
    h_chart.add("6 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=6)).count())
    h_chart.add("7 days", Features.objects.filter(tag="Feature Request", development_status="Currently Being Investigated", published_date=timezone.now().date() - timedelta(days=7)).count())
    chart8 = h_chart.render_data_uri()
    
    
    return render(request, 'stats.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3, 'chart4': chart4, 'chart5': chart5, 'chart6': chart6, 'chart7': chart7, 'chart8': chart8})