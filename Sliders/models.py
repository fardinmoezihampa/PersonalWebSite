from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان اسلایدر')
    descriptions = models.CharField(max_length=200, verbose_name='توضیحات اسلایدر')
    url = models.URLField(verbose_name='آدرس اسلایدر')
    image = models.ImageField(upload_to='images/sliders/', verbose_name='تصویر اسلایدر')
    is_show = models.BooleanField(verbose_name='نمایش داده شود ؟')
    fade_up_image = models.ImageField(upload_to='images/sliders/fades', verbose_name='تصویر متحرک')

    class Meta:
        ordering = ['title']
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'لیست اسلایدرها'

    def __str__(self):
        return f'silders :{self.title}'
