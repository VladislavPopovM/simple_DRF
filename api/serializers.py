from rest_framework import serializers
from .models import Investor, Passport, Qualification

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id','login_name', 'accept_rules')

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ('id','first_name', 'second_name', 'middle_name', 'numb_pass', 'born_date', 'place_born', 'get_pass_date', 'department_code', 'issued_by', 'reg_address', 'photo','investor')

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id','status', 'photo', 'investor')