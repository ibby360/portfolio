from projects.models import Projects
from django.shortcuts import render, get_object_or_404
from projects.models import Projects, Projectimages
from blog.models import Post

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    posts = Post.objects.filter(status='published').order_by('-publish')
    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'index.html', context)
