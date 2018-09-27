from django.db import models
from django.db.models import Sum

class Company(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_total_office_rent(self):
        rent = Office.objects.filter(company=self).aggregate(Sum('monthly_rent'))
        return rent.get('monthly_rent__sum', 0.0)

class Office(models.Model):
    company = models.ForeignKey(Company,related_name='offices', on_delete=models.CASCADE)
    street = models.CharField('Street', max_length=256, blank=True)
    postal_code = models.CharField('Postal Code', max_length=32, blank=True)
    city = models.CharField('City', max_length=128, blank=True, null=True)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    is_headquarter = models.BooleanField('Is headquarter', default=False)

    def __str__(self):
        return self.street
