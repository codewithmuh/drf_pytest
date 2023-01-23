import factory
from api.models import Song

class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song
    
    title = factory.Faker("sentence")
    artist = factory.Faker("name")
    lyrics = factory.Faker("text")
    file_location = factory.Faker("slug")
    