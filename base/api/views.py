from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()  # Fetch all rooms
    serializer = RoomSerializer(rooms, many=True)  # Serialize multiple objects
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    try:
        room = Room.objects.get(id=pk)  # Fetch a single room
        serializer = RoomSerializer(room, many=False)  # Serialize a single object
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response({"error": "Room not found"}, status=404)  # Handle case where room doesn't exist
