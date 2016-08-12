from rest_framework import serializers


class GetInfoSerializer(serializers.Serializer):
    pincode = serializers.IntegerField(max_value=999999)
    money_limit = serializers.IntegerField()