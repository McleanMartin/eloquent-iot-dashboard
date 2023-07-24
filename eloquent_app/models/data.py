from django.db import models


class DeviceData(models.Model):
    device = models.ForeignKey(Device, related_name='device', on_delete=models.CASCADE)
    field_1 = models.CharField(('data port 1'), max_length=10, null=True, blank=False)
    field_2 = models.CharField(('data port 2'), max_length=10, null=True, blank=False)
    field_3 = models.CharField(('data port 3'), max_length=10, null=True, blank=False)
    field_4 = models.CharField(('data port 4'), max_length=10, null=True, blank=False)
    field_5 = models.CharField(('data port 5'), max_length=10, null=True, blank=False)
    field_6 = models.CharField(('data port 6'), max_length=10, null=True, blank=False)
    field_7 = models.CharField(('data port 7'), max_length=10, null=True, blank=False)
    field_8 = models.CharField(('data port 8'), max_length=10, null=True, blank=False)
    field_9 = models.CharField(('data port 9'), max_length=10, null=True, blank=False)
    field_10 = models.CharField(('data port 10'), max_length=10, null=True, blank=False)

    class Meta:
        verbose_name = ("DeviceData")
        verbose_name_plural = ("DeviceData")

    def __str__(self):
        return self.device

    def get_absolute_url(self):
        return reverse("Data_detail", kwargs={"pk": self.pk})
