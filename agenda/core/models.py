from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação do Evento')

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo