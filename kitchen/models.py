from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField("Меню", max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('kitchen:choice_list_by_menu',
                           args=[self.slug])


class Choice(models.Model):
    menu = models.ForeignKey(Menu,
                                 related_name='wide_choice',
                                 on_delete=models.CASCADE)
    name = models.CharField("Наименование блюд", max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='wide_choice/%Y/%m/%d',
                              blank=True)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Стоимость, руб.", max_digits=10, decimal_places=2)
    available = models.BooleanField("Внесение в прайс", default=True)
    created = models.DateTimeField("Дата внесения", auto_now_add=True)
    updated = models.DateTimeField("Дата изменения", auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('kitchen:choice_detail',
                           args=[self.id, self.slug])