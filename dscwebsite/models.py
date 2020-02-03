from django.db import models

# Create your models here.

class services(models.Model):
    serv_name = models.CharField(max_length=50)
    serv_desc = models.TextField()

class events(models.Model):
    ev_name = models.CharField(max_length=50)
    ev_desc = models.CharField(max_length=2000)
    ev_date = models.DateTimeField()
    ev_reg_end = models.DateField()
    ev_img = models.ImageField(upload_to='pics')
    ev_availability = models.BooleanField(default=True)
    ev_year = models.IntegerField()


class hof(models.Model):
    hof_name = models.CharField(max_length=50)
    hof_desc = models.TextField()
    hof_awards = models.CharField(max_length=5000)
    hof_img = models.ImageField(upload_to='pics')
    hof_yr = models.IntegerField()

class team(models.Model):
    tm_name = models.CharField(max_length=50)
    tm_exp = models.CharField(max_length=50)
    tm_desc = models.CharField(max_length=5000)
    tm_img = models.ImageField(upload_to='pics')
    tm_ph = models.IntegerField()
    tm_mail = models.EmailField(max_length=250)
