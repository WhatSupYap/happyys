from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..models import Monster 


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def get_monster_list(request):
    #data = {'message': 'Hello, REST API!'}
    # json 객체 만들고 싶어

    # monster_list = Monster.objects.all() 로 받아온 객체를 json으로 변환
    monster_list = Monster.objects.all()
    monster_list = list(monster_list.values())
    data = {'monster_list': monster_list}
    return Response(data)

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def create_monster(request):
    if request.method == 'POST' or request.method == 'GET':
        # 받아온 데이터를 사용하여 Monster 모델의 정보를 저장
        name = request.query_params['name']
        desc = request.query_params['desc']
        # 이미 저장된 이름인지 확인
        if Monster.objects.filter(name=name).exists():
            return Response({'message': 'Monster with the same name already exists'})
        monster = Monster(name=name, desc=desc)
        monster.save()
        return Response({'message': 'Monster saved successfully'})
    else:
        return Response({'message': 'Invalid request method'})