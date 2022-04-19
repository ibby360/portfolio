from projects.models import Projects
from django.contrib import admin
 
 
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
 
    class Meta:
       model = Projects
 