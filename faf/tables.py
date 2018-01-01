# tutorial/tables.py
import django_tables2 as tables
from .models import MotoricsFactors


class MotoricsStrenghtTable(tables.Table):
    class Meta:
        model = MotoricsFactors
        template = 'django_tables2/bootstrap.html'
        fields = ('date', 'strength')


class MotoricsEnduranceTable(tables.Table):
    class Meta:
        model = MotoricsFactors
        template = 'django_tables2/bootstrap.html'
        fields = ('date', 'endurance')


class MotoricsVelocityTable(tables.Table):
    class Meta:
        model = MotoricsFactors
        template = 'django_tables2/bootstrap.html'
        fields = ('date', 'velocity')


class MotoricsCoordinationTable(tables.Table):
    class Meta:
        model = MotoricsFactors
        template = 'django_tables2/bootstrap.html'
        fields = ('date', 'coordination')
