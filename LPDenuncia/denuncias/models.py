from django.db import models
class PersonaDenuncinate(models.Model):
    Nombre=models.CharField(max_length=120,verbose_name='Nombre del denunciante')
    Appellido=models.TextField(max_length=200,verbose_name='Apellido del denunciante')
    Telefono=models.IntegerField()
    TonoDePiel=models.CharField(max_length=120,verbose_name='Color de piel del denunciante')
    Edad=models.IntegerField()
    ColorOjos=models.CharField(max_length=100,verbose_name='Color de los ojos')
    Estatura=models.FloatField(max_length=4, verbose_name='Estatura del denunciante')
    Relacion=models.TextField(max_length=200,verbose_name='La relacion entre el denunciante y el desaparecido')
    def __str__(self):
        return self.Nombre
class PersonaDesaparecida(models.Model):
    Nombre=models.CharField(max_length=120,verbose_name='Nombre del desaparecido')
    Appellido=models.TextField(max_length=200,verbose_name='Apellido del desaparecido')
    Telefono=models.IntegerField()
    TonoDePiel=models.CharField(max_length=120,verbose_name='Color de piel del desaparecido')
    Edad=models.IntegerField()
    ColorOjos=models.CharField(max_length=100,verbose_name='Color de los ojos')
    Estatura=models.FloatField(max_length=4, verbose_name='Estatura del desapareido')
    PersonaDesaparecida=models.ManyToManyField(PersonaDenuncinate)
    def __str__(self):
        return self.Nombre

class UltimoAvistamiento(models.Model):
    DescripcionLugar=models.TextField(max_length=200,verbose_name='Descripcion del lugar donde desaparecio')
    Rango_Horario=models.TextField(max_length=200,verbose_name='Rango visto por ultima vez')
    Ropa =models.TextField(max_length=200,verbose_name='Ropa del desaparecido')
    Ubicacion=models.TextField(max_length=200,verbose_name='Ubicacion del avistamiento')
    PersonaDesaparecida=models.ForeignKey(PersonaDesaparecida, on_delete=models.CASCADE)

class Sospecho(models.Model):
    Apareiencia=models.TextField(max_length=200,verbose_name='Apariencia del sospechoso')
    Motivo=models.TextField(max_length=200,verbose_name='Motivo de sospecha')
    Sospecho=models.ForeignKey(PersonaDesaparecida, on_delete=models.CASCADE)

class ReportarAparecimiento(models.Model):
    Condicion=models.TextField(max_length=200,verbose_name='Condicion de salud')
    Ropa=models.TextField(max_length=200,verbose_name='Condicion de salud')
    Fotografia= models.ImageField(upload_to='Aparecidos/%Y/%m/%d', null=True, blank=True)
    PersonaDesaparecida=models.ForeignKey(PersonaDenuncinate, on_delete=models.CASCADE)
