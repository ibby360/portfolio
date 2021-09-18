from projects.models import Projects, Projectimages
from django.contrib import admin
 
class ProjectsImageAdmin(admin.StackedInline):
    model = Projectimages
 
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectsImageAdmin]
 
    class Meta:
       model = Projects
 
@admin.register(Projectimages)
class ProjectsImageAdmin(admin.ModelAdmin):
    pass