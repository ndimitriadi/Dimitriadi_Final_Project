from django.db import models

class Testimonial(models.Model):

    star_options = [
        (1, '1 Star - ★☆☆☆☆'),
        (2, '2 Stars - ★★☆☆☆'),
        (3, '3 Stars - ★★★☆☆'),
        (4, '4 Stars - ★★★★☆'),
        (5, '5 Stars - ★★★★★'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    stars = models.IntegerField(default=5, choices=star_options)

    def __str__(self):
        return self.name
