from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Project


# Create your views here.

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'spacider/index.html', context)

def report(request, pk):
    project = get_object_or_404(Project, pk=pk)
    content = {
        'pid': pk,
        'project': project
    }
    return render(request,'spacider/report.html', content)

def compare(request):
    if request.method == 'POST':
        print request.POST.getlist(u'_selected_action') # this code is important getlist() method
    return None



