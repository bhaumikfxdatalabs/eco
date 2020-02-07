import os
import random
from djongo import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)

    return "products/{new_filename}".format(
        new_filename=new_filename)


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=40.00)
    quantity = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to=upload_image_path)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.DjongoManager()

    def __str__(self):
        return self.name
