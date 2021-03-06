from django.db import models
from utils.models import generate_unique_slug


class Brand(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=210, default='', blank=True)

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(Brand, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Бренды'


class Option(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Опции'


class AutoManagerVolvo(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(brand__title='Volvo')


class Auto(models.Model):
    AUTO_CLASS_ECONOMY = 'e'
    AUTO_CLASS_COMFORT = 'c'
    AUTO_CLASS_BUSINESS = 'b'

    AUTO_CLASS_CHOICES = (
        (AUTO_CLASS_ECONOMY, 'economy'),
        (AUTO_CLASS_COMFORT, 'comfort'),
        (AUTO_CLASS_BUSINESS, 'business'),
    )
    objects = models.Manager()
    objects_volvo = AutoManagerVolvo()
    brand = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE, related_name='cars')
    options = models.ManyToManyField(Option, related_name='cars')
    number = models.CharField(max_length=15)
    description = models.TextField(max_length=2, default='', blank=True)
    year = models.SmallIntegerField(null=True)
    auto_class = models.CharField(max_length=1, null=True, choices=AUTO_CLASS_CHOICES, default=AUTO_CLASS_ECONOMY)

    def __str__(self):
        return self.number

    def display_options(self):
        return ', '.join([option.title for option in self.options.all()[:3]])
    display_options.short_description = 'Options'

    def display_engine_power(self):
        return self.pts.engine_power
    display_engine_power.short_description = 'Engine power'

    class Meta:
        verbose_name_plural = 'Автомобили'


class VehiclePassport(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE, related_name='pts', verbose_name=Auto._meta.verbose_name)
    vin = models.CharField(max_length=30, verbose_name='Идентификационный номер (VIN)')
    engine_volume = models.SmallIntegerField(verbose_name='Объем двигателя, куб.см')
    engine_power = models.SmallIntegerField(verbose_name='Мощность двигателя, л.с.')

    def __str__(self):
        return f'{self.auto}::{self.vin}'

    class Meta:
        verbose_name_plural = 'Паспорта машин'

