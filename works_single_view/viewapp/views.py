from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Song
from .serializers import SongSerializer
from .import_csv import load_csv_file
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        title = request.GET.get('title', None)

        if title is not None:
            songs = songs.filter(title__icontains = title)
        
        songs_serializer = SongSerializer(songs, many=True)
        return JsonResponse(songs_serializer.data, safe=False)
 
    elif request.method == 'POST':
        load_csv_file("song.csv")
        return JsonResponse({'message': 'songs data were imported successfully!'},status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        count = Song.objects.all().delete()
        return JsonResponse({'message': '{} songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    print(pk, "(((___")
    try: 
        song = Song.objects.get(pk=pk) 
    except Song.DoesNotExist: 
        return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        song_serializer = SongSerializer(song) 
        return JsonResponse(song_serializer.data) 
 
    elif request.method == 'PUT': 
        song_data = JSONParser().parse(request) 
        song_serializer = SongSerializer(song, data=song_data) 
        if song_serializer.is_valid(): 
            song_serializer.save() 
            return JsonResponse(song_serializer.data) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        song.delete() 
        return JsonResponse({'message': 'song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def song_list_iswc(request):
    songs = Song.objects.exclude(iswc='')
        
    if request.method == 'GET': 
        songs_serializer = SongSerializer(songs, many=True)
        return JsonResponse(songs_serializer.data, safe=False)