from django.db import models

# Create your models here.
class QuestionLatin2japanese(models.Model) :
    japanese_text = models.CharField(max_length=200)
    latin_text = models.CharField(max_length=200)

    def __str__(self):
        return self.latin_text