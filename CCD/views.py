from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from CCD.serializers import MonitoringSerializer
# from rest_framework.permissions import IsAuthenticated


class MonitoringAddView(CreateAPIView):
    serializer_class = MonitoringSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
