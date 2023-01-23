from dataclasses import fields
from api.models import Song

from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'lyrics', 'file_location']