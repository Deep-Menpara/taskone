from django.db import models

# Create your models here.
class data(models.Model):
    id=models.AutoField(primary_key=True, serialize=False, verbose_name='ID')
    subid=models.IntegerField(default=0)
    subcategory = models.TextField()
    title=models.TextField()
    price=models.IntegerField()
    popularity=models.IntegerField()