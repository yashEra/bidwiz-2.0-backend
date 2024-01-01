from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):
    routes = [
        "api/register",
        "api/login",
        "api/login/refresh",
        "api/logout",
    ]
    return Response(routes)
