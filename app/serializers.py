from rest_framework import serializers
from app.models import PortfolioProject


class ProjectSerializer(serializers.ModelSerializer):

    class Meta: #Metaconfig
        model = PortfolioProject #model=databasename
        fields = ['title', 'technoligies_used', 'github_link', 'project_description'] #shown fields
