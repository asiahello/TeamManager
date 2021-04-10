from django.utils import timezone
from django.db import models

# Create your models here.
from user.models import Player

ANALYSIS_CATEGORIES = (
    ('TACTICAL', 'TAKTYCZNE'),
    ('TECHNICAL', 'TECHNICZNE'),
    ('MOTORICAL', 'MOTORYCZNE'),
    ('MENTAL', 'MENTALNE'),
    ('SOMATICAL', 'SOMATYCZNE'),
)

SWOT_CATEGORIES = {
    ('STRENGTH', 'MOCNE STRONY'),
    ('WEAKNESS', 'S?ABE STRONY'),
    ('UNKNOWN', 'NIEPRZYPISANE')
}


class SwotAnalysis(models.Model):
    update_date = models.DateTimeField(
        verbose_name="Ostatnio zmienione",
        default=timezone.now,
        null=True
    )
    owner = models.OneToOneField(
        Player,
        verbose_name="Autor",
        related_name="swot",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.owner.user.username


class AnalysisSubCategory(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="nazwa",
    )

    def __str__(self):
        return self.name


class Factor(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='nazwa',
    )
    analysis_category = models.CharField(
        max_length=15,
        verbose_name="kategoria",
        choices=ANALYSIS_CATEGORIES,
        null=True,
    )
    analysis_subcategory = models.ForeignKey(
        AnalysisSubCategory,
        verbose_name="podkategoria",
        related_name="factors",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name


class PlayerFactor(models.Model):
    factor = models.ForeignKey(
        Factor,
        verbose_name="czynnik",
        related_name='player_factors',
        on_delete=models.CASCADE,
        null=True,
    )
    swot_category = models.CharField(
        max_length=15,
        verbose_name="klasyfikacja",
        choices=SWOT_CATEGORIES,
        default='UNKNOWN',
    )
    swot_analysis = models.ForeignKey(
        SwotAnalysis,
        verbose_name="Analiza SWOT",
        related_name="player_factors",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.factor.name







