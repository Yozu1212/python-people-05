from django.db import models

class peopledata(models.Model):
    statistic_yyymm = models.CharField(max_length=100)
    svillage = models.IntegerField(default=0)
    household_no = models.IntegerField(default=0)
    people_total = models.IntegerField(default=0)
    birth_total = models.IntegerField(default=0)
    death_m = models.IntegerField(default=0)
    death_f = models.IntegerField(default=0)
    def __str__(self):
        return self.svillage

    def __str__(self):
        return self.name
    
class cpdata(models.Model):
    year = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.title

