from django.core.validators import ValidationError


def max_value_validator(value):
    if value > 100:
        raise ValidationError('مقدار ورودی بیش از حد مجاز است تصحیح شود')


def min_value_validator(value):
    if value < 0:
        raise ValidationError('مقدار ورودی کتر از حد مجاز است تصحیح شود')
