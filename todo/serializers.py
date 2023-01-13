from rest_framework import serializers
from todo.models import Todo


#투두 조회
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'year', 'month', 'day','done', 'writer']

        
#투두 생성
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'year', 'month', 'day', 'writer')
        
#투두 수정
class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'year', 'month', 'day','done', 'writer')