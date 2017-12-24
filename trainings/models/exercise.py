from django.db import models
from django.contrib.auth.models import User


class TechniqeCatManager(models.Manager, ):
    def get_queryset(self):
        return super(TechniqeCatManager, self).get_queryset().filter(category='techniqe')


class TacticsCatManager(models.Manager):
    def get_queryset(self):
        return super(TacticsCatManager, self).get_queryset().filter(category='tactics')


class MotoricsCatManager(models.Manager):
    def get_queryset(self):
        return super(MotoricsCatManager, self).get_queryset().filter(category='motorics')


class OtherCatManager(models.Manager):
    def get_queryset(self):
        return super(OtherCatManager, self).get_queryset().filter(category='other')


class AgeCategory(models.Model):

    name = models.CharField(max_length=20, verbose_name="kategoria")

    class Meta:
        verbose_name = "Kategoria wiekowa"
        verbose_name_plural ="Kategoria wiekowa"
    def __str__(self):
        return self.name


class Exercise(models.Model):

    # image
    # link to youtube

    CAT = (
        ('techniqe', 'Technika'),
        ('tactics', 'Taktyka'),
        ('motorics', 'Motoryka'),
        ('other', 'Inna'),
    )

    category = models.CharField(max_length=20, choices=CAT, default='other', verbose_name="kategoria")
    # jak po tym wyszukiwać
    # subcategory = models.ForeignKey(TrainingSubcategory, on_delete=models.SET_NULL, null=True, blank=True, default="")
    title = models.CharField(max_length=250, verbose_name="Tytuł", blank=True, default="")
    description = models.TextField(verbose_name="opis", blank=True, default="")
    duration = models.IntegerField(verbose_name="czas trwania", blank=True, default="")
    author = models.ForeignKey(User, related_name='autor', on_delete=models.SET_NULL, null=True, verbose_name="autor", blank=True, default="")
    age_category = models.ForeignKey(AgeCategory, blank=True, default="")

    # objects = models.Manager()  # default manager
    techniqe = TechniqeCatManager()
    tactics = TacticsCatManager()
    motorics = MotoricsCatManager()
    other = OtherCatManager()

    # class Meta:
    #     ordering = ('-date',)
    #     app_label = 'trainings'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('trainings:ex_detail', kwargs={'ex_id': self.pk})
