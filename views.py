from django.shortcuts import render
from rest_framework import viewsets
from .models import Backend
from .models import School
from .models import Scholarship
from .models import Tuition_Fees

from .serializers import BackendSerializer
from .serializers import SchoolSerializer
from .serializers import ScholarshipSerializer
from .serializers import Tuition_FeesSerializer

from django.http import HttpResponse

class BackendView(viewsets.ModelViewSet):
    queryset = Backend.objects.all()
    serializer_class = BackendSerializer
class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
class ScholarshipView(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
class Tuition_FeesView(viewsets.ModelViewSet):
    queryset = Tuition_Fees.objects.all()
    serializer_class = Tuition_FeesSerializer



def donorform(request):
    return render(request, 'backend/donorform.html')


