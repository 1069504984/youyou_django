from rest_framework import serializers

from .models import Person

# from utils import validates



class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
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
        model = Person
        fields = ('first_name',"last_name")


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

class ProjectsRunSerializer(serializers.ModelSerializer):
    """
    运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      )

    class Meta:
        model = Person
        fields = ('id', 'first_name')
