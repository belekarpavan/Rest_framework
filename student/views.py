from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse,multipartparser
from . models import student
from .serializers import studentSerializers

# Create your views here.

class register(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self,request):
        serializer=studentSerializers
        return Response({'serializer': serializer})
    def post(self,request):
        serializer = studentSerializers(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return redirect('student_data')


class viewData(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'show.html'

    def get(self, request):
        queryset = student.objects.all()
        return Response({'student': queryset})

class editData(APIView) :

    def get(self,request,pk):
        stud=get_object_or_404(student,pk=pk)
        stud.delete()
        return redirect('student_data')
    def post(self,request,pk):
        return redirect('student_update',pk)



class updatestud(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'update.html'

    def get(self,request,pk):
        stud = get_object_or_404(student, pk=pk)
        serializer = studentSerializers(stud)
        return Response({'serializer': serializer, 'profile': stud})

    def post(self,request,pk):
        stud = get_object_or_404(student, pk=pk)
        serializer = studentSerializers(stud, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': stud})
        serializer.save()
        return redirect('student_data')
