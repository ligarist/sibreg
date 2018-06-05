from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

SHORT_TEXT_LEN = 500



# Модель продукта
class Cook(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='cook/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cook:CookDetail', args=[self.id, self.slug])

    def get_short_text(self):
        if len(self.description) > SHORT_TEXT_LEN:
            return self.description[:SHORT_TEXT_LEN]
        else:
            return self.description
