import sys, os
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NogiSongRecommender.settings")

import django
django.setup()

from Reviews.models import SongReview, NogizakaSong


def save_review_from_row(review_row):
    review = SongReview()
    review.id = review_row[0]
    review.user_name = review_row[1]
    review.song = NogizakaSong.objects.get(id=review_row[2])
    review.rating = review_row[3]
    review.publish_date = datetime.datetime.now()
    review.comment = review_row[4]
    review.save()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Reading from file" + str(sys.argv[1]))
        review_df = pd.read_csv(sys.argv[1])
        print(review_df)

        review_df.apply(save_review_from_row, axis=1)

        print("There are {} reviews in DB.".format(SongReview.objects.count()))

    else:
        print("Please, provide Reviews file path.")    