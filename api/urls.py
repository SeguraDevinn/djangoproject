from django.urls import path
from .views import CandlestickData, lineChartData, barChartData, pieChartData


#These are the patterns for the URL for the API endpoints
urlpatterns = [
    path('candlestick-data/', CandlestickData.as_view(), name='candlestick-data'),
    path('line-chart-data/', lineChartData.as_view(), name='line-chart-data'),
    path('bar-chart-data/', barChartData.as_view(), name='bar-chart-data'),
    path('pie-chart-data/', pieChartData.as_view(), name='pie-chart-data'),
]