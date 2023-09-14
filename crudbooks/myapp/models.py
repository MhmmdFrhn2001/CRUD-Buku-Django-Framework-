from django.db import models

class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.CharField(db_column='author', max_length=100,  blank=False, null=False)
    year = models.IntegerField(db_column='year',blank=False, default=2000)

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

# Create your models here.
