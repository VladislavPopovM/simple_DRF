from django.db import models

# Create your models here.

class Investor(models.Model):
    login_name = models.CharField(max_length=32)
    status_qua = models.BooleanField(default=False)
    accept_rules = models.BooleanField(default=False)

    def __str__(self):
        return self.login_name

class Passport(models.Model):
    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    numb_pass = models.PositiveBigIntegerField()
    born_date = models.DateField()
    place_born = models.CharField(max_length=128)
    get_pass_date = models.DateField()
    department_code = models.PositiveIntegerField()
    issued_by = models.CharField(max_length=128)
    reg_address = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='passports/')
    investor = models.OneToOneField('Investor', on_delete=models.CASCADE)

class Qualification(models.Model):
    status = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='passports/')
    investor = models.OneToOneField('Investor', on_delete=models.CASCADE)