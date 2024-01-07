from django.db import models

class Title(models.Model):
    title = models.CharField(max_length=255)

class Text(models.Model):
    title = models.CharField(max_length=255)

class HeaderText(models.Model):
    body = models.TextField(max_length=255)

class HeaderImg(models.Model):
    img = models.ImageField()

class About(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)

class Services(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)


class Portfolio(models.Model):
    body = models.TextField(max_length=255)
    text = models.TextField(max_length=255)

class Price(models.Model):
    body = models.TextField(max_length=255)
    text = models.CharField(max_length=255)
    price = models.TextField(max_length=255)
