# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 11:37
# @Author  : Fighter
from rest_framework import serializers

from .models import Traffic

# from utils import validates



class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Traffic
        exclude = ('update_time', )

        extra_kwargs = {
            'create_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project_obj = super().create(validated_data)


        return project_obj


class ProjectNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traffic
        fields ="__all__"


# class InterfaceNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Interfaces
#         fields = ('id', 'name')
#
#
# class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
#     interfaces = InterfaceNameSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Projects
#         fields = ('id', 'interfaces')


