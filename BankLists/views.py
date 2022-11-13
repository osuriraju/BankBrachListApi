from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import BankListSerializer
from .models import BanksList
from rest_framework.decorators import api_view


@api_view()
def index(request):
    return Response({'Info': 'In the url, enter the branch name after the main url to get the bank details Ex : mainURL/branch'})



class BankBranchClass(viewsets.ReadOnlyModelViewSet):
    serializer_class = BankListSerializer

    def get_queryset(self):

        #Loading all the data from db
        
        banks_data = BanksList.objects.all()
        return banks_data

    def retrieve(self, request, *args, **kwargs):
        
        #Accessing the request parameter and filtering

        params = kwargs
        banks = BanksList.objects.filter(branch__iexact = params['pk'])
        serializer = BankListSerializer(banks, many = True)

        return Response(serializer.data)