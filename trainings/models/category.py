from django.db import models





class TrainingCategory(models.Model):

    CAT = (
        ('techniqe', 'Technika'),
        ('tactics', 'Taktyka'),
        ('motorics', 'Motoryka'),
        ('other', 'Inna'),
    )

    name = models.CharField(max_length=20, choices=CAT, default='other', verbose_name="kategoria")



    class Meta:
        verbose_name = "Kategoria"

    def __str__(self):
        return self.name


class TrainingSubcategory(models.Model):

    name = models.CharField(max_length=20, default="", blank=True, verbose_name="kategoria")

    class Meta:
        verbose_name = "Podkategoria"

    def __str__(self):
        return self.name


# class CategoryManager(models.Manager):

#     def get_queryset(self):
#         return CategoryQuerySet(self.model, using=self._db)

#     def techniqe(self):
#         return self.get_queryset().techniqe()

#     def tactics(self):
#         return self.get_queryset().tactics()

#     def motorics(self):
#         return self.get_queryset().motorics()

#     def other(self):
#         return self.get_queryset().other()




# class CategoryQuerySet(models.QuerySet):

#     def techniqe(self):
#         return self.filter(name='techniqe')

#     def tactics(self):
#         return self.filter(name='tactics')

#     def motorics(self):
#         return self.filter(name='motorics')

#     def other(self):
#         return self.filter(name='other')