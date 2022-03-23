from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.apps import apps

IGNORED_NAMES = ["LogEntry", "Permission", "Group", "User", "ContentType", "Session", "Dummy"]
rows = 20


@api_view(['GET'])
def test(request):
	return Response("hello")

@api_view(['GET'])
def getTableData(request, name):
	model = apps.get_model('api', name)
	table = model.objects.order_by("?")[:rows]
	serializer = model.serialize(list(table.values()))
	return Response(serializer.data)

@api_view(['GET'])
def getTableNames(request):
	models = [model.__name__ for model in apps.get_models() if model.__name__ not in IGNORED_NAMES]
	return Response(models)

@api_view(['POST'])
def postTableData(request, name):
	model = apps.get_model('api', name)
	serializer = model.serialize(request.data)
	# print(request.data)
	# print(serializer)
	# serializer.save()
	# return Response(request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors)
