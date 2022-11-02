from api.models import RinCommands
from api.serializers import RinCommandsModuleSerializer, RinCommandsSerializer
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView


class GetAllCommands(mixins.ListModelMixin, generics.GenericAPIView):
    """
    Gets all of the commands available in Rin
    """

    queryset = RinCommands.objects.all()
    serializer_class = RinCommandsSerializer

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetModuleCommands(APIView):
    """
    Get each command that a module/cog has
    """

    def get_object(self, cog: str):
        try:
            return RinCommands.objects.filter(cog=cog)
        except RinCommands.DoesNotExist:
            raise Http404

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def get(self, request, cog):
        command = self.get_object(cog)
        serializer = RinCommandsSerializer(command, many=True)
        return Response(serializer.data)


class GetAllModules(APIView):
    """
    Returns a list of all of the cogs that Rin has
    """

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        queryset = RinCommands.objects.all().order_by().distinct("cog")
        serializer = RinCommandsModuleSerializer(queryset, many=True)
        mainData = serializer.data
        responseData = [item["cog"] for item in mainData]
        return Response(responseData)
