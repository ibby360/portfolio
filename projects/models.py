from django.db import models
from django.db.models.fields import TextField
from taggit.managers import TaggableManager

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

class Projectimages(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    images = models.FileField(upload_to='project/images/')

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

    def __str__(self):
        return self.project.title
    