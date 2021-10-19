from django.db import models
# Create your models here.
from django.db import models

from bulk_update_or_create import BulkUpdateOrCreateQuerySet

# from django_mysql.models import ListCharField
from django.contrib.postgres.fields import ArrayField


class Brand(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    b_name = models.CharField(max_length=100, null=True, blank=True)
    official_link = models.URLField(max_length=500, null=True, blank=True)
    activity = models.CharField(max_length=200, null=True, blank=True)
    about_brand = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True, default = '')
    reference = models.URLField(max_length=500, null=True, blank=True) 
    brand_understanding = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)


    def __str__(self):
        return f'{self.b_name}'


class Popular_products_by_brands(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    b_name = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE) 
    p_name = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.b_name} -- {self.p_name}'

class Most_used_notes_by_brand(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    b_name = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=True, blank=True)
    accord = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.b_name} -- {self.accord,self.score}'


class All_fragnances_by_brand(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    b_name = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.b_name} -- {self.name}'    


class Products(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    b_name = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200, null=True, blank=True)
    p_image = models.URLField(max_length=500, null=True, blank=True)
    sex = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    reference = models.URLField(max_length=500, null=True, blank=True)
    colour = models.CharField(max_length=200, null=True, blank=True)
    time = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return f'{self.b_name} -- {self.p_name}'


class Main_accords(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    score = models.FloatField(null=True, blank=True)
    accord = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.p_name}'


class Occasion(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    sport = models.PositiveIntegerField(null=True, blank=True)
    night_out = models.PositiveIntegerField(null=True, blank=True)
    evening = models.PositiveIntegerField(null=True, blank=True)
    leisure = models.PositiveIntegerField(null=True, blank=True)
    daily = models.PositiveIntegerField(null=True, blank=True)
    business = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.p_name}'


class Similar_products(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    link = models.URLField(max_length=500, null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.p_name} -- {self.name}'


class Audience(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    young = models.PositiveIntegerField(null=True, blank=True)
    old = models.PositiveIntegerField(null=True, blank=True)
    men = models.PositiveIntegerField(null=True, blank=True)
    women = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.p_name}'


class Seasons(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    winter = models.FloatField(null=True, blank=True)
    summer = models.FloatField(null=True, blank=True)
    spring = models.FloatField(null=True, blank=True)
    fall = models.FloatField(null=True, blank=True)
    day = models.FloatField(null=True, blank=True)
    night = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f'{self.p_name}'


class Product_notes(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    p_name = models.ForeignKey(Products, null=True, blank=True, on_delete=models.CASCADE)
    top_note = models.TextField(null=True, blank=True)
    middle_note = models.TextField(null=True, blank=True)
    base_note = models.TextField(null=True, blank=True)
    others = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.p_name}'


class Wifi_perfuma(models.Model):
    classname = models.CharField(max_length=500, null=True, blank=True)
    ingredients = models.CharField(max_length=300, null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.classname}'
    