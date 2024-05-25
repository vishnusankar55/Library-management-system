from django.shortcuts import render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

@permission_classes([IsAdminUser])
class LibrarianView(APIView):
    def get(self, request):
        return Response({"message": "This is the librarian view."})

@permission_classes([IsAuthenticated])
class CustomerView(APIView):
    def get(self, request):
        return Response({"message": "This is the customer view."})


