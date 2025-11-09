from django.db import models

class NASPOItem(models.Model):
    vendor = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    manufacturer_part_number = models.CharField(max_length=255, blank=True, null=True)
    list_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    naspo_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.vendor} - {self.description[:50] if self.description else ''}"
