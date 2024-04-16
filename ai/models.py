from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


def validate_square_image(image):
    if image.width != image.height:
        raise ValidationError("Стороны изображения должны быть равны!")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя пользователя (ваше имя, '
                                                                             'отображаемое на сайте)',
                                default='Пользователь', unique='True')
    slug = models.SlugField(unique=True, blank=True, db_index=True,
                            verbose_name='URL (пример: имя_пользователя)')
    first_name = models.CharField(default='name', max_length=100, verbose_name='Никнейм')
    last_name = models.CharField(default='surname', max_length=100, verbose_name='Фамилия')
    email = models.EmailField(default='example@gmail.com', verbose_name='Эл. почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Фото профиля', validators=[validate_square_image])

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Профили пользователей'
