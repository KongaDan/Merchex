from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name=models.fields.CharField(max_length=100)
    
    biography=models.fields.CharField(max_length=1000,default='')
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2021)],null=True)
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)
    class Genre(models.TextChoices):
        AETHER='ae'
        LUMINE='lu'
        MORAX='zonghli'
        RAIDEN='ei'
    genre=models.fields.CharField(choices=Genre.choices,max_length=10,default='ae' )
    def __str__(self) -> str:
        return f'{self.name}'
    
class Listing(models.Model):
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=100, default='not description yet')
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(null=True)
    type = models.fields.CharField(max_length=100, default='incown')
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return f'{self.title}'