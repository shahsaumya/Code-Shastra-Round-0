from rest_framework import serializers
from hunt_app.models import Team, Task

class TeamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Team
		fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = '__all__'