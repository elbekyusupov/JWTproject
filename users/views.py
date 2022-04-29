from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, serializers, mixins
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializer import UserSerializer, ConditionSerializer
from .models import User, Condition
import jwt, datetime

# Create your views here.
class UserView(APIView):
    def get(self, request):
        user = User.objects.filter(phone = request.user.phone).first()
        return Response({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone
        })
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        data = request.data
        user = User.objects.filter(phone = request.user.phone).first()
        serializer = UserSerializer(instance=user, data=data, partial =True)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ConditionView(APIView):
    def post(self, request):
        serializer = ConditionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, request, id):
        data = request.data
        con = Condition.objects.filter(id = id).first()
        serializer = ConditionSerializer(instance = con, data=data, partial =True)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

        


class ConditionListView(generics.ListAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    # def get(self, request):
    #     con = Condition.objects.all()
    #     return Response({
    #         'id': con.id,
    #         'name': con.name,
    #         'desc': con.desc,
    #     }, many = True)
    
class ConditionRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionRetrieveView(generics.RetrieveAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionRetrieveDestroyView(generics.RetrieveDestroyAPIView,):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionViewMixin(mixins.ListModelMixin, generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Condition.objects.all()
    print(queryset)
    serializer_class = ConditionSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


