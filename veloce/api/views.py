from api.models import RinCommands
from api.serializers import RinCommandsModuleSerializer, RinCommandsSerializer
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView


class GetAllCommands(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RinCommands.objects.all()
    serializer_class = RinCommandsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetModuleCommands(APIView):
    def get_object(self, cog: str):
        try:
            return RinCommands.objects.filter(cog=cog)
        except RinCommands.DoesNotExist:
            raise Http404

    def get(self, request, cog):
        command = self.get_object(cog)
        serializer = RinCommandsSerializer(command, many=True)
        return Response(serializer.data)


class GetAllModules(APIView):
    def get(self, request):
        queryset = RinCommands.objects.all().order_by().distinct("cog")
        serializer = RinCommandsModuleSerializer(queryset, many=True)
        mainData = serializer.data
        responseData = [item["cog"] for item in mainData]
        return Response(responseData)
