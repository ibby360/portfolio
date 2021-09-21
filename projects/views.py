from projects.models import Projects
from django.shortcuts import render, get_object_or_404
from projects.models import Projects, Projectimages

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)
