from django.db import models


# Create your models here.
class Payment(models.Model):
    card_number = models.BigIntegerField(unique=True)
    card_type = models.CharField(max_length=30)
    billing_address = models.CharField(max_length=1000)

    objects = models.Manager()

    class Meta: 
        ordering = ['-card_number']
        
def create_process(_card_number, _card_type, _billing_address):
    payment = Payment(card_number=_card_number, card_type=_card_type, billing_address=_billing_address)

    # Validation - Ensure the instance values comply with those of the model definition
    # Rasie ValidationError if the test failed
    payment.full_clean()
    
    # Create the record in the target database
    payment.save()

def fetch_all_pmt_methods_process():
    # Return a dict of payment methods
    return Payment.objects.in_bulk()
    
def fetch_payment_process(_id):
    return Payment.objects.get(id=_id)

def edit_process(_id, _card_number, _card_type, _billing_address):
    Payment.objects.filter(id=_id).update(card_number=_card_number, card_type=_card_type,
        billing_address=_billing_address)

def delete_process(_id):
    Payment.objects.filter(id=_id).delete()