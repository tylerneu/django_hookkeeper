import datetime
from django.db import models

class Klass(models.Model):
    name = models.CharField(max_length=100)
    # abbreviation
    weight = models.IntegerField()
    
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    
    def __unicode__(self):
        return "{} {}".format(self.weight, self.name)
        
class Tractor(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name;

class Pull(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.today)
    classes = models.ManyToManyField(Klass, related_name="classes")

    def __unicode__(self):
        return self.name;
    
    def class_count(self):
        return len(self.classes.all())


class Entry(models.Model):
    pull = models.ForeignKey(Pull)
    klass = models.ForeignKey(Klass)
    tractor = models.ForeignKey(Tractor)
    order = models.IntegerField()
    # hooks
    # driver
    
    def __unicode__(self):
        return "{}, {}, {}".format(self.pull, self.klass, self.tractor);

