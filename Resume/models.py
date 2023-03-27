from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import min_value_validator, max_value_validator


class Skill(models.Model):
    skill = models.CharField(max_length=50, verbose_name='عنوان مهارت')
    # percent = models.IntegerField(verbose_name='درصد تسلط در مهارت',
    #                               validators=[MinValueValidator(0, 'مقدار ورودی کمتر از حد مجاز است'),
    #                                           MaxValueValidator(100, 'مقدار ورودی بیشتر از حد مجاز است')])

    percent = models.IntegerField(verbose_name='درصد تسلط در مهارت',
                                  validators=[min_value_validator, max_value_validator])

    class Meta:
        ordering = ['-percent']
        verbose_name = 'مهارت'
        verbose_name_plural = 'لیست مهارت ها'

    def __str__(self):
        return f'skill : {self.skill}'


class Biography(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام مهارت')
    avatar = models.ImageField(upload_to='images/resume/bio/', verbose_name='تصویر آواتار')
    description = models.TextField(verbose_name='متن بیوگرافی')
    is_active = models.BooleanField(verbose_name='فعال باشد؟', default=False)

    class Meta:
        verbose_name = 'بیوگرافی'
        verbose_name_plural = 'لیست بیوگرافی ها'

    def __str__(self):
        return f'bio :{self.title}'
