from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import employees
from rest_framework import viewsets
from .serializers import employeesSerializer
from django.http import HttpResponse

# Create your views here.

class pavan(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = employeesSerializer





#HTML Views

#Rendering HTML

class empList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile.html'

    def get(self, request):
        queryset = employees.objects.all()
        return Response({'emp': queryset})

#Rendering Forms

class PavanList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        emp = get_object_or_404(employees, pk=pk)
        serializer = employeesSerializer(emp)
        return Response({'serializer': serializer, 'profile': emp})

    def post(self, request, pk):
        emp = get_object_or_404(employees, pk=pk)
        serializer = employeesSerializer(emp, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': emp})
        serializer.save()
        return redirect('profile')

