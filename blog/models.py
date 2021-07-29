from django.db import models


CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    postdate = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY, default='ビジネス', null=True
    )

    def __str__(self):
        return self.title