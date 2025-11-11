from django.db import models

class Guest(models.Model):
    """
    يمثل بيانات النزيل المسجل في النظام.
    """
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    unit_number = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - وحدة {self.unit_number}"