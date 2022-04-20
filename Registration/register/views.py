from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import JsonResponse
import json
# from urllib import request

# Create your views here.

class Signup(APIView):
    def post(self, request):
        if request.method =='POST':
            # body = request.get_json()
            data=json.loads(request.body)
            print(data)
        # hashed_password = generate_password_hash(body['password'], method = 'sha256')
        # new_user = Users(public_id=str(uuid.uuid4()), first_name=body['first_name'], last_name=body['last_name'], email = body['email'], dob= body['dob'], password=hashed_password, is_active = False)
        
        return JsonResponse({
            'message': 'Registeration Successfull'
            })
