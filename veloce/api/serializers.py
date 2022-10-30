from api.models import RinCommands
from rest_framework import serializers


class RinCommandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RinCommands
        fields = ["name", "description", "cog"]


class RinCommandsModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RinCommands
        fields = ["cog"]
