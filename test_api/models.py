from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    number = models.IntegerField()
    operators = models.ManyToManyField('Operator', through='User_operators')


class Sensor(models.Model):
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    resque = models.ForeignKey('ResqueTeam')




class Operator(models.Model):
    name = models.CharField(max_length=50)



class ResqueTeam(models.Model):
    type = models.CharField(max_length=100)
    number = models.IntegerField()


class Territory(models.Model):
    square = models.IntegerField()
    coor_start = models.CharField(max_length=15)
    coor_end = models.CharField(max_length=15)
    operators = models.ManyToManyField('Operator', through='Oper_on_terr')
    sensor = models.ForeignKey('Sensor')

class User_operators(models.Model):
    user = models.ForeignKey('User')
    operator = models.ForeignKey('Operator')

class Oper_on_terr(models.Model):
    territory = models.ForeignKey('Territory')
    operator = models.ForeignKey('Operator')

