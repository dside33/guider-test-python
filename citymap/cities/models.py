from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Город {self.name}"

class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return f"Улица {self.name}"

class Shop(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='shops')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='shops')
    house_number = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"Магазин {self.name}"
