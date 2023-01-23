from django.shortcuts import redirect, render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from api import serializers
from api.models import Song
from api.serializers import SongSerializer

class SongListView(APIView):

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print(request.data)
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/song')
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = Song.objects.get(pk=pk)
        serializer = SongSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/song')
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = Song.objects.get(pk=pk)
        obj.delete()
        return redirect('/song')


class ListView(generics.ListCreateAPIView):

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
