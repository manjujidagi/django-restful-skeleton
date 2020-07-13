# Create your views here.
from users.models import User
from users.serializers import UserSerializer


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

import jwt
from datetime import datetime
import os
import json
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'config', 'jwt_config.json')) as jwt_config_file:
    jwt_config = json.load(jwt_config_file)

@csrf_exempt
def users_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def user_login(request):
    
    if request.method == 'POST':
        data = JSONParser().parse(request)

        try:
            user = User.objects.get(username=data['username'], password=data['password'])
            serializer = UserSerializer(user)
        except User.DoesNotExist:
            return JsonResponse({"error_id" : "", "error_detail" : "Username or Password Mismatch"}, status=400)

        token_payload = dict(serializer.data)
        token_payload["created"] = str(datetime.now())

        # Return Token
        ret_json_data = {
            "token" : (jwt.encode(token_payload, jwt_config["secret"], algorithm=jwt_config["algorithm"])).decode('ascii')
        }

        print(ret_json_data["token"])

        return JsonResponse(ret_json_data)