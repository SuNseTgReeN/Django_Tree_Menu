from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('menu:menu_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
