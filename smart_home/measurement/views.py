from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SensorSerializer(request.data)
        sen = Sensor(name=ser.data['name'], description=ser.data['description'])
        sen.save()
        return Response(ser.data)


class DetailView(APIView):
    def get_object(self, pk):
        return Sensor.objects.get(id=pk)

    def patch(self, request, pk):
        sensor = self.get_object(pk)
        ser = SensorSerializer(instance=sensor, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({'status': 'Произошла ошибка!'})

    def get(self, request, pk):
        sensor = self.get_object(pk)
        sen = SensorDetailSerializer(sensor, )
        return Response(sen.data)


class MeasurementsView(APIView):
    def post(self, request):
        ser = MeasurementSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)