from django.db import models

# Create your models here.
class project(models.Model):
    titulo=models.CharField(max_length=50, verbose_name="titulo")
    descripcion=models.TextField(verbose_name="descripcion")
    imagen=models.ImageField(verbose_name="imagen",upload_to='project')
    crear=models.DateTimeField(auto_now_add=True, verbose_name="fecha crear")
    actualizar=models.DateTimeField(auto_now=True, verbose_name="fecha actualizar")
    url=models.URLField(verbose_name="Direccion web", null=True, blank=True)
    
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=["-crear"]
    
    def __str__(self):
        return self.titulo
    