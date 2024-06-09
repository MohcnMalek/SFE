from django.db import models

class ChargePointExtra(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define primary key field
    serial = models.CharField(max_length=50, default='')
    model = models.CharField(max_length=50, default='')
    station = models.CharField(max_length=100, default='')
    joindate = models.DateField(default='')  # Example default date
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.serial} - {self.model} - {self.station}"
 
class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifiant_bancaire = models.CharField(max_length=50, default='')
    station = models.CharField(max_length=100, default='')
    type_of_vehicle = models.CharField(max_length=50, default='')
    joindate = models.DateField(default='')  # Exemple de date par défaut
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Ajout du champ montant
    status = models.BooleanField(default=False)
    energy = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.identifiant_bancaire} - {self.station} - {self.type_of_vehicle} - {self.energy} kWh"
    
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=255, default='')
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    functions = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.email
    
class ChargingSession(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('process', 'In Process')
    ]

    bank_id = models.CharField(max_length=20)
    chargepoint_id = models.BigAutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50,default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    payment_method = models.CharField(max_length=50,default='')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='')

    def __str__(self):
        return f'{self.bank_id} - {self.chargepoint_id} - {self.status}'