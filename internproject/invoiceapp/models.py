from django.db import models

# Create your models here.
class Invoice(models.Model):
    Date=models.DateTimeField(auto_now=True)
    Invoice_customerName=models.CharField(max_length=100)

    def __str__(self) :
        return '%s'% self.Invoice_customerName
class InvoiceDetail(models.Model):
    invoice_id=models.IntegerField()
    description=models.CharField(max_length=400)
    quantity=models.IntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=4)
    price=models.DecimalField(max_digits=10,decimal_places=4)