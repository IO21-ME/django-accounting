from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150)

    # address
    address_line_1 = models.CharField(max_length=128)
    address_line_2 = models.CharField(max_length=128,
                                      blank=True, null=True)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=7)
    country = models.CharField(max_length=50)

    # optionnaly linked to an organization
    # for automated behaviors during cross-organizations invoicing
    organization = models.ForeignKey('books.Organization',
                                     blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.name