# from django.shortcuts import render

from rest_framework import viewsets
from api.models import Checkbox
from api.serializers import CheckboxSerializer, DataSerializer, DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics, mixins
from api.utils import Sum

class Checkboxlist(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAdminUser]
    queryset=Checkbox.objects.all()
    serializer_class=CheckboxSerializer
    def get(self, req, *args, **kwargs):
        # users=[user.username for user in User.objects.all()]
        # return Response(users)
        # users=User.objects.all()
        # serializer=UserSerializer(users, many=True)
        # return Response(serializer.data)
        # checkboxes=Checkbox.objects.all()
        # serializer=CheckboxSerializer(checkboxes, many=True)
        # return Response(serializer.data)
        return self.list(req, *args, **kwargs)

    def post(self, req, *args, **kwargs):
        # serializer=CheckboxSerializer(data=req.data)
        # if serializer.is_valid():
        #     serializer.save()
        # return Response(serializer.data, status.HTTP_201_CREATED)
        return self.create(req, *args, **kwargs)

# class CheckboxDetailed(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Checkbox.objects.all()
#     serializer_class=CheckboxSerializer
#     def delete(self,req,pk,format=None):
#         checkbox=Checkbox.objects.get(id=pk)
#         checkbox.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 



class CheckboxViewSet(viewsets.ModelViewSet):
    queryset=Checkbox.objects.all()
    serializer_class=CheckboxSerializer

@api_view(['GET'])
def checkbox_list(req):
    # api={'a':2, 'b':3}
    checkboxes=Checkbox.objects.all()
    serializer=CheckboxSerializer(checkboxes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def checkbox_detail(req, pk):
    try:
        checkbox=Checkbox.objects.get(id=pk)
        serializer=CheckboxSerializer(checkbox)
    except Checkbox.DoesNotExist:
        return Response({'error': f'Checkbox with id={pk} is not found'} ,status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['POST'])
def checkbox_create(req):
    serializer=CheckboxSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['PUT'])
def checkbox_update(req, pk):
    try:
        checkbox=Checkbox.objects.get(id=pk)
        serializer=CheckboxSerializer(checkbox, data=req.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist:
        return Response({'error': f'Checkbox with id={pk} is not found'} ,status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(['DELETE'])
def checkbox_delete(req, pk):
    checkbox=Checkbox.objects.get(id=pk)
    checkbox.delete()
    # serializer=CheckboxSerializer(checkbox, data=req.data)
    return Response(status=status.HTTP_204_NO_CONTENT)

class DateView(APIView):

    @staticmethod
    def get(req):
        serializer=DataSerializer(data=req.query_params)
        serializer.is_valid(raise_exception=True)
        result=Sum(serializer.validated_data).call()
        return Response(result, status=status.HTTP_200_OK)

