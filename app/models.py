from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=100)
    owner_email = models.EmailField()
    employee_size = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Business_detail'

class Businesss(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(primary_key=True)
    firstname = models.TextField(blank=True, null=True, db_comment='changes')

    class Meta:
        managed = True  # Set to True to allow Django to manage the table
        db_table = 'business_name' 
    