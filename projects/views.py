from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Person
from . import serializers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.ProjectNamesModelSerializer
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ['name', 'leader', 'tester']
    ordering_fields = ['id']
    # permission_classes = [permissions.IsAuthenticated]

    # 在实际项目中, 如何创建接口呢?
    # 1. 优先使用框架提供的功能
    # 2. 如果框架提供的功能不满足需要
    # a. 如果只有少量的地方不满足, 可以拓展父类提供的方法
    # b. 如果绝大多数的地方都不满足, 就自己实现
    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     # datas = get_count_by_project(serializer.data)
        #     return self.get_paginated_response(datas)
        #
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        # print(1/0)
        response = super().list(request, *args, **kwargs)
        # response.data['results'] = get_count_by_project(response.data['results'])
        return response

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    # @action(detail=True)
    # def interfaces(self, request, pk=None):
    #     interface_obj = Interfaces.objects.filter(project_id=pk)
    #     one_list = []
    #     for obj in interface_obj:
    #         one_list.append({
    #             "id": obj.id,
    #             "name": obj.name
    #         })
    #     return Response(data=one_list)




    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return  response


