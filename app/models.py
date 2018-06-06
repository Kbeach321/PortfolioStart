from django.db import models

# Create your models here.

class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    technoligies_used = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    project_description = models.TextField() # models.TextField()
