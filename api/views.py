from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#The following functions are used to define the endpoints for my API.
#The data is hardcoded and each function does the same thing, stores and then returns the 
#data as a Response

class CandlestickData(APIView):
    def get(self, request):
        data = {
            "data": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
                {"x": "2023-01-03", "open": 45, "high": 60, "low": 30, "close": 50},
                {"x": "2023-01-04", "open": 45, "high": 50, "low": 20, "close": 35}

            ]
        }
        return Response(data)


class lineChartData(APIView):
    def get(self, request):
        data = {
            
                "labels": ["Jan", "Feb", "Mar", "Apr"],
                "data": [10, 15, 5, 25]
        }
            

        return Response(data)
    
class barChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [50, 10, 100]
        }
        
        return Response(data)
    
class pieChartData(APIView):
    def get(self, request):
        data = {
            "labels": ["Red", "Blue", "Yellow"],
            "data": [200, 50, 100]
        }
        return Response(data)