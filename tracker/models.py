from django.db import models

class Price(models.Model):
    asset = models.CharField(max_length=100, null=True)  # Asset name (e.g., Bitcoin, Ethereum)
    price = models.FloatField()               # Current price
    timestamp = models.DateTimeField()        # Timestamp for the price

    def __str__(self):
        return f"{self.asset} - {self.price}"
