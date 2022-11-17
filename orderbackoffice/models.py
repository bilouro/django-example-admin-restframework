import uuid

from django.db import models

# Create your models here.

STATUS = (
    ('1', 'Proposal'),
    ('2', 'Accepted'),
    ('3', 'Work in Progress'),
    ('4', 'Done'),
    ('5', 'Archived'),
)

class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Customer Name")
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Phone(models.Model):
    number = models.CharField(max_length=20, verbose_name="Phone number")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.number

class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4)
    date = models.DateTimeField('date')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=STATUS, default='1')

    def __str__(self):
        return '%s - %s' % (self.customer.name, str(self.order_id))


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Service Name")

    def __str__(self):
        return self.name

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    payed = models.BooleanField(blank=True)
    done = models.BooleanField(blank=True)

    def __str__(self):
        return self.service.name
