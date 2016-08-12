from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Area, Company, Delivery
from .serializers import GetInfoSerializer
import json


class GetInfoAPIView(views.APIView):

    serializer_class = GetInfoSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            pincode = int(data.get('pincode'))
            pincode = get_object_or_404(Area, pincode=pincode)
            money_limit = int(data.get('money_limit'))
            delivery = Delivery.objects.filter(
                Q(pincode=pincode) &
                (Q(price__gte=money_limit) | Q(price=0))
                )
            name = []
            for x in delivery:
                name.append(str(x.company))

            return Response({
                'company': name
            })
        else:
            return Response({
                'message': 'bas request'
            })
