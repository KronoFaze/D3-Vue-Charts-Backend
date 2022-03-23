from django.db import models
from rest_framework import serializers

class Dummy(models.Model):

	date = models.DateField(db_column='Date', blank=True, null=True)
	month = models.CharField(db_column='Month', max_length=3, blank=True, null=True)
	district_name = models.CharField(db_column='District_name', max_length=16, blank=True, null=True)
	sales = models.IntegerField(db_column='Sales', blank=True, null=True)  

	class Meta:
		managed = False
		db_table = 'dummy'
	
	def serialize(self):
		serializer = DummySerializer(data=self, many=True)
		if serializer.is_valid():
			return serializer
		return serializer.errors

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
			return serializer
		return serializer.errors

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__" 

class Sales(models.Model):
	date = models.DateField()
	month = models.CharField(max_length=3)
	district_name = models.CharField(max_length=16)
	sales = models.IntegerField()  

	def serialize(self):
		serializer = SalesSerializer(data=self, many=True)
		if serializer.is_valid():
			return serializer
		return serializer.errors

class SalesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sales
		fields = "__all__" 

class Employee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()  
	dob = models.DateField()
	salary = models.IntegerField()  
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)

	def serialize(self):
		serializer = EmployeeSerializer(data=self, many=True)
		if serializer.is_valid():
			return serializer
		return serializer.errors

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = "__all__" 
