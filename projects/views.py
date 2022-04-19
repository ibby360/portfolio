from projects.models import Projects
from django.shortcuts import render
from projects.models import Projects

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context)
