from django.db import models

# Create your models here.


class Travel(models.Model):
    title = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.title


class Step(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    data_step = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return self.city


class Stopover(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title