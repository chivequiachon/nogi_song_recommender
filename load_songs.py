import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NogiSongRecommender.settings")

import django
django.setup()

from Reviews.models import NogizakaSong


def save_song_from_row(song_row):
    song = NogizakaSong()
    song.id = song_row[0]
    song.romaji_title = song_row[1]
    song.kanji_title = song_row[2]
    song.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        songs_df = pd.read_csv(sys.argv[1])
        print(songs_df)

        songs_df.apply(
            save_song_from_row,
            axis=1
        )

        print("There are {} songs".format(NogizakaSong.objects.count()))
        
    else:
        print("Please, provide Nogi song file path")