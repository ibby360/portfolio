from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = TaggableManager()
    image = models.ImageField(upload_to='project/image', blank=True, null=True )
    project_link = models.CharField(max_length=250, null=True, blank=True)
    github_repo = models.CharField(max_length=250, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
