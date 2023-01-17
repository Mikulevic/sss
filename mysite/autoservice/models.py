from django.db import models

class Automobilio_modelis():
    marke = models.CharField(verbose_name="Markė", max_length=100)
    modelis = models.CharField(verbose_name="Modelis", max_length=100)



class Automobilis():
    valst_numeris = models.CharField(verbose_name="Valstybinis numeris")
    auto_modelis = models.ForeignKey(to="Automobilio_modelis", on_delete=models.SET_NULL)
    vin = models.CharField(verbose_name="VIN kodas", max_length=17)
    klientas = models.CharField(verbose_name="Klientas", max_length=100)


class Paslauga():
    pavadinimas = models.CharField(verbose_name="Pavadinimas", max_length=100)
    kaina = models.FloatField(verbose_name="kaina")

class Uzsakymas():
    data = models.CharField(verbose_name="Data")
    automobilis_id = models.ForeignKey(to="Automobilio_modelis", on_delete=models.CASCADE)
    kiekis = models.IntegerField(verbose_name="Kiekis")

class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey(to="Uzsakymas", on_delete=models.CASCADE)
    paslauga = models.ForeignKey(to="Paslauga", on_delete=models.SET_NULL, null=True)
