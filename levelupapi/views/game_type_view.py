"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import GameType
from rest_framework.status import HTTP_404_NOT_FOUND


class GameTypeView(ViewSet):
    """Level up game types"""

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = GameType.objects.all()

        # Note the additional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        game_types = GameTypeSerializer(
            game_types, many=True, context={'request': request})
        return Response(game_types.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            game_type = GameType.objects.get(pk=pk)
            game_type = GameTypeSerializer(game_type, context={'request': request})
            return Response(game_type.data)
        except GameType.DoesNotExist:
            return Response({'message': 'Game Type does not Exist'}, status=HTTP_404_NOT_FOUND)

class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields =  '__all__' # ('id', 'label')
