from gettext import install
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    short_desciption = models.TextField()
    published_at = models.DateField()

class Director(models.Model):
    first_name = models.CharField(verbose_name="imię", max_length=100)
    last_name = models.CharField(verbose_name="nazwisko", max_length=100)
    about = models.TextField(verbose_name="o reżyserze", blank=True)
    photo = models.ImageField(verbose_name="zdjęcie", blank=True)

class Meta:
    ordering = ["last_name", "first_name"]
    verbose_name = "reżyser"
    verbose_name_plural = "reżyserzy"

def __str__(self):
    return "Reżyser: " + self.first_name + " " + self.last_name

class Movie(models.Model):
    title = models.CharField(verbose_name="tytuł", max_length=100)
    short_description = models.TextField(verbose_name="opis")
    published_at = models.DateField(verbose_name="data premiery")
# !!!
director = models.ForeignKey(
    to="movies.Director",
    verbose_name="reżyser",
    related_name="movies",
    on_delete=models.CASCADE,
    null=True
)

class Meta:
    ordering = ["title"]
    verbose_name = "film"
    verbose_name_plural = "filmy"

def __str__(self):
    return "Film: " + self.title



