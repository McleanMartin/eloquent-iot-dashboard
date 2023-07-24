from django.db import models


class DeviceData(models.Model):

    

    class Meta:
        verbose_name = ("DeviceData")
        verbose_name_plural = ("DeviceData")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Data_detail", kwargs={"pk": self.pk})
