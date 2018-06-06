
###########MODELS (TABLES) IMPORTS###################
from app.models import PortfolioProject
##############SERIALIZER IMPORTS################
from app.serializers import ProjectSerializer

#########V1 FRAMEWORK IMPORTS######################
from rest_framework.views import APIView
from rest_framework.response import Response

############ LIST VIEW / CREATE NEW ################

class PortfolioListAPIVIEW(APIView):
    def get(self, request):              # RETURNS A LIST OF PROJECTS #
        all_portfolios = PortfolioProject.objects.all()
        serialized_portfolios = ProjectSerializer(all_portfolios, many=True)
        return Response(serialized_portfolios.data)

    def post(self, request): #CREATES A NEW PROJECT #
        print(request.POST)
        title = request.POST['title']
        technoligies_used = request.POST['technoligies_used']
        github_link = request.POST['github_link']
        project_description = request.POST['project_description']

        PortfolioProject.objects.create(title=title, technoligies_used=technoligies_used,
                                github_link=github_link, project_description=project_description)
        return Response({})

################ SINGLE OBJECT READ[get] / UPDATE[put] / DELETE[delete]###############

class PortfolioDetailAPIView(APIView):
    def get(self, request, pk):
        portfolioproject = PortfolioProject.objects.get(id=pk)
        serialized_portfolios = ProjectSerializer(portfolioproject)
        return Response(serialized_portfolios.data)

    def put(self, request, pk):
        portfolioproject = PortfolioProject.objects.get(id=pk)
        portfolioproject.title = request.POST['title']
        portfolioproject.technoligies_used = request.POST['technoligies_used']
        portfolioproject.github_link = request.POST['github_link']
        portfolioproject.project_description = request.POST['project_description']
        portfolioproject.save()
        return Response({})

    def delete(self,request, pk):
        portfolioproject = PortfolioProject.objects.get(id=pk)
        portfolioproject.delete()
        return Response({})
