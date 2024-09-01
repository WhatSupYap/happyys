from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from ..models import Sogsag



@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def set_sogsag(request):
    if request.method == 'POST':

        content = request.data.get('content')
        if content is None:
            return Response({'message': 'Content is missing'}, status=400)
        # 이미 저장된 이름인지 확인
        sogsag = Sogsag(content=content)
        sogsag.save()
        return Response({'message': 'sogsag saved successfully'})
    else:
        return Response({'message': 'Invalid request method'})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_sogsag_list(request):
    if request.method == 'GET':
        #sogsag = Sogsag.objects.all()
        #sogsag = Sogsag.objects.filter(status='R').order_by('-reg_date')
        sogsag = Sogsag.objects.filter(status=0).order_by('-reg_date')
        sogsag_list = list(sogsag.values())
        data = {'sogsag_list': sogsag_list}
        return Response(data)
    else:
        return Response({'message': 'Invalid request method'})

@api_view(['DELETE'])
@permission_classes([AllowAny])
def del_sogsag(request, sogsag_id):
    if request.method == 'DELETE':
        sogsag = get_object_or_404(Sogsag, id=sogsag_id)
        sogsag.delete()
        return Response({'message': 'sogsag deleted successfully'})
    else:
        return Response({'message': 'Invalid request method'})
    
#for sogsag in Sogsag.objects.all():
#    sogsag.delete()
    

#@api_view(['POST'])
@permission_classes([AllowAny])
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file is None:
            return Response({'message': 'File is missing'}, status=400)
        # Save the file
        # Assuming you have a 'files' directory in your project
        file_path = f'files/{file.name}'
        with open(file_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return Response({'message': 'File uploaded successfully'})
    else:
        return Response({'message': 'Invalid request method'})