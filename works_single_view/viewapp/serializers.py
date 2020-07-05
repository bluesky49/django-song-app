from rest_framework import serializers 
from viewapp.models import Song
 
 
class SongSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Song
        fields = ('id',
                  'title',
                  'contributor',
                  'iswc')