from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from todo.models import Todo
from todo.serializers import TodoSerializer, TodoCreateSerializer, TodoUpdateSerializer

import json

class TodoAPIView(APIView):
    #조회
    def get(self, request):
        #사용자로부터 데이터 받기(year, month)
        body = json.loads(request.body)
        d_year = body["year"]
        d_month = body["month"]
        
        data = Todo.objects.filter(writer=str(request.user), year=d_year, month=d_month).values() #적절한 데이터 검색
        return Response({"resultCode":200,"data":data}, status=status.HTTP_200_OK)
    
    #추가
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"resultCode":200,"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
    
	#수정
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)

        if todo.writer != str(request.user): #작성자 일치여부 확인
            return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
        
        #수정작업
        serializer = TodoUpdateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"resultCode":200,"data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
    
    #삭제
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        
        if todo.writer != str(request.user): #작성자 일치여부 확인
            return Response({"resultCode":500}, status=status.HTTP_400_BAD_REQUEST)
        
        #삭제작업
        todo.delete()
        return Response({"resultCode":200},status=status.HTTP_204_NO_CONTENT)