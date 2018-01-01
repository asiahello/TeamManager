from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from faf.models import SomaticsFactors


class SomaticsChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, player_id, param):
        user_somatics_factors = SomaticsFactors.objects.user_params(player_id)

        if param == "weight":
            data = [{'x': sf.date, 'y': sf.weight} for sf in user_somatics_factors]
        elif param =="fat":
            data = [{'x': sf.date, 'y': sf.fat} for sf in user_somatics_factors]
        elif param == "bmi":
            data = [{'x': sf.date, 'y': sf.bmi} for sf in user_somatics_factors]
        else:
            data = None

        return [DataSet(
            type='line',
            label='Time Series',
            borderColor='black',
            data=data,
        )]
