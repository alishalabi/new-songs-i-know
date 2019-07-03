from django.test import TestCase

from .models import Song
# Create your tests here.


class SongModelTests(TestCase):
    def able_to_create_one_song_objects(self):
        song = Song('Hello Goodbye', 'Beatles', 'someUrl', 'anotherUrl',
                    'someTab', 'someLyrics')
        self.assertIsInstance(song, Song)

    def able_to_create_three_song_objects(self):
        song1 = Song('Hello Goodbye', 'Beatles', 'someUrl', 'anotherUrl',
                     'someTab', 'someLyrics')
        song2 = Song('Elenor Rigby', 'Beatles', 'someUrl', 'anotherUrl',
                     'someTab', 'someLyrics')
        song3 = Song('While My Guitar Gently Wheeps', 'Beatles', 'someUrl', 'anotherUrl',
                     'someTab', 'someLyrics')
        all_songs = [song1, song2, song3]
        self.assertEqual(len(all_songs), 3)

# song_name = models.CharField(max_length=200)
# artist = models.CharField(max_length=200)
# youtube_tutorial = models.CharField(
#     max_length=300, blank=True, default='')
# song_tab = models.CharField(max_length=100, blank=True, default='')
# lyrics = models.CharField(max_length=2000, blank=True, default='')
# experience_level
