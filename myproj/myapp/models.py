from django.db import models


class tech(models.Model):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    count = models.IntegerField()
    date_of_Delivery = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.model)
    


class tech_img(models.Model):
    tech = models.ForeignKey(tech, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="myapp/static/img")


# Create your models here.
