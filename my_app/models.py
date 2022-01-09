from django.db import models
from django.urls import reverse


class robots(models.Model):
    tipo = models.CharField(max_length=300)
    lote = models.CharField(max_length=300)
    last_updated = models.DateTimeField(auto_now_add=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.nome)

    def status(self):
        return [self.nome, self.tipo, self.created, self.lote]