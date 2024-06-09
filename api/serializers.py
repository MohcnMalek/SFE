from rest_framework import serializers
from chargepoint.models import ChargePointExtra, Client, Users, ChargingSession

class ChargePointExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePointExtra
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ChargingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingSession
        fields = '__all__'
