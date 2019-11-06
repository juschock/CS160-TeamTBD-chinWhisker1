from django.db import models

# Create your models here.


class Shaver(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    type = models.CharField(max_length=30) #may be an error // type = forms.ChoiceField(choices=RAZORS)
    qty = models.IntegerField()
    shave_image = models.URLField()
   
    objects = models.Manager()
    
    class Meta:
        unique_together = ['brand', 'model']

def create_process(_brand, _model, _color, _type, _qty, _shave_image):
    shaver = Shaver(brand=_brand, model=_model, color=_color, type=_type, qty=_qty, shave_image=_shave_image )

    # Validation - Ensure the instance values comply with those of the model definition
    # Rasie ValidationError if the test failed
    shaver.full_clean()
    
    # Create the record in the target database
    shaver.save()

def fetch_all_shavers_process():
    # Return a dict of songs
    return Shaver.objects.in_bulk()

def fetch_shaver_process(_id):
    return Shaver.objects.get(id=_id)

def edit_process(_id, _brand, _model, _color, _type, _qty, _shave_image):
    Shaver.objects.filter(id=_id).update(brand=_brand, model=_model, color=_color, type=_type, qty=_qty, shave_image=_shave_image )

def delete_process(_id):
    Shaver.objects.filter(id=_id).delete()