# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, get_object_or_404

from .models import Sensor, Measurement
from .serializers import SensorSerializers, MeasurementSerializer, SensorDetailSerializer,MeasurementCreateSerializer

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializers

class MeasurmentCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.prefetch_related('measurements')
    serializer_class = SensorDetailSerializer
