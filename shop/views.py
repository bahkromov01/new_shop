
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Category


# Create your views here.

class CategoryList(APIView):

    def get(self, request):
        categories = [category.title for category in Category.objects.all()]
        return Response(categories)