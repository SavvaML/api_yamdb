from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
from titles.models import Titles


class Review(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True,
                                    db_index=True,
                                    verbose_name='Дата публикации отзыва')
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="aut_review",
                               verbose_name='Автор отзыва')
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])
    title = models.ForeignKey(Titles,
                              blank=True,
                              on_delete=models.CASCADE,
                              related_name="tit_review",
                              verbose_name='Оценка произведения')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('author', 'title')
        ordering = ["pub_date"]

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE,
                               related_name="comment",
                               verbose_name='Автор комментария')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name="comment",
                               verbose_name='Оценка комментария')
    text = models.TextField(blank=False,
                            verbose_name='Текст комментария')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации комментария',
                                    db_index=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["pub_date"]
        verbose_name='Комментарии'
