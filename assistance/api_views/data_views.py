import traceback

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from assistancems.utils.resp_tools import Resp
from rest_framework.pagination import PageNumberPagination

import requests

class DataView(APIView):

    def get(self, request, format=None):

        
        token = None
        try:
            token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        except:
            print("Error")

        headers = {'Authorization': 'Bearer {}'.format( token )}
        response = requests.get('http://127.0.0.1:8000/api/auth/verify/', headers = headers)
        print( response )

        return Resp(
                
        ).send()