from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from chargepoint.models import ChargePointExtra, Client, Users, ChargingSession
from .serializers import ChargePointExtraSerializer, ClientSerializer, UsersSerializer, ChargingSessionSerializer

@api_view(['GET'])
def get_chargepoints(request):
    chargepoints = ChargePointExtra.objects.all()
    serializer = ChargePointExtraSerializer(chargepoints, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_charging_sessions(request):
    sessions = ChargingSession.objects.all()
    serializer = ChargingSessionSerializer(sessions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def boot_notification(request):
    data = request.data
    # Process the boot notification data
    # For example, you can save or update the ChargePointExtra model
    chargepoint, created = ChargePointExtra.objects.update_or_create(
        serial=data.get('charge_point_model'),
        defaults={'model': data.get('charge_point_vendor')}
    )
    return Response({"message": "BootNotification received"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def status_notification(request):
    data = request.data
    # Process the status notification data
    # For example, you can update the status of the ChargePointExtra model
    ChargePointExtra.objects.filter(serial=data.get('connector_id')).update(status=data.get('status'))
    return Response({"message": "StatusNotification received"}, status=status.HTTP_200_OK)
