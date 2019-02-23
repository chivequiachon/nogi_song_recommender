from django.db import models


class NogizakaSong(models.Model):
    romaji_title = models.CharField(max_length=50)
    kanji_title = models.CharField(max_length=50)

    def average_rating(self):
        all_ratings = list(map(lambda x: x.rating, self.review_set.all()))
        return np.mean(all_ratings)

    def __str__(self):
        return "{} ({})".format(self.romaji_title, self.kanji_title)


class SongReview(models.Model):
    RATING_CHOICES = (
        (1, '1')
        (2, '2')
        (3, '3')
        (4, '4')
        (5, '5')
    )

    song = models.ForeignKey(NogizakaSong, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
