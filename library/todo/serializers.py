from rest_framework.serializers import HyperlinkedModelSerializer

from todo.models import Projects, ProjectsTodo
from users.serializers import UsersModelSerializer


class TodosModelSerializer(HyperlinkedModelSerializer):
    user = UsersModelSerializer()

    class Meta:
        model = ProjectsTodo
        fields = ('description', 'user', 'status',)


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UsersModelSerializer(many=True)
    todos = TodosModelSerializer(many=True)

    class Meta:
        model = Projects
        fields = ('title', 'link', 'users', 'todos',)
