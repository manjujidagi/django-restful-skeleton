# Create your views here.
from rental.models import Friend, Belonging, Borrowed
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def friends_list(request):

    if request.method == 'GET':
        friends = Friend.objects.all()
        serializer = FriendSerializer(friends, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FriendSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)