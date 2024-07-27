from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200, verbose_name= 'Titulo')
    description = models.TextField(verbose_name= 'Descripción')
    image = models.ImageField(upload_to='projects', default= 'https://www.shutterstock.com/image-vector/default-image-icon-vector-missing-260nw-2086941550.jpg', verbose_name= 'Imagen')
    create = models.DateTimeField(auto_now_add= True, verbose_name= 'Fecha de creación')
    update = models.DateTimeField(auto_now= True, verbose_name= 'Fecha de edición')
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-create"]
        
    def __str__(self):
        return self.title