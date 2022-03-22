from django.db import models
from rest_framework import serializers

class Dummy(models.Model):

	date = models.DateField(db_column='Date', blank=True, null=True, serialize=True)
	month = models.CharField(db_column='Month', max_length=3, blank=True, null=True)
	district_name = models.CharField(db_column='District_name', max_length=16, blank=True, null=True)
	sales = models.IntegerField(db_column='Sales', blank=True, null=True)  

	class Meta:
		managed = False
		db_table = 'dummy'
	
	def serialize(self):
		serializer = DummySerializer(data=self, many=True)
		if serializer.is_valid():
			return serializer.data

class DummySerializer(serializers.ModelSerializer):
	class Meta:
		model = Dummy
		fields = "__all__"

class Student(models.Model):
	name = models.CharField(max_length=20)
	dob = models.DateField()
	marks = models.IntegerField()

	def serialize(self):
		serializer = StudentSerializer(data=self, many=True)
		if serializer.is_valid():
			return serializer.data

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__" 