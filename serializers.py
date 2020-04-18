from rest_framework import serializers
from .models import Backend
from .models import School
from .models import Scholarship
from .models import Tuition_Fees

class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backend
        fields = ('id', 'name', 'paradigm')
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('schoolID', 'school_name', 'school_address', 'city',
                  'country_province', 'type_of_school','em_contact',
                  'em_contact_num1', 'em_contact_num2')
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ('scholarshipID', 'denomination', 'referred_studies', 'amount',
                  'academic_year', 'description')
class Tuition_FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition_Fees
        fields = ('schoolID', 'academic_level', 'academic_year', 'tuition',
                  'clothing', 'furniture','books', 'misc')

