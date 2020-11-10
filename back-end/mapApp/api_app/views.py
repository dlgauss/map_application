from rest_framework import viewsets, permissions
from rest_framework.response import  Response
from .serializers import ItsmIncidentsSerializer, CommentSCreateSerializer, IncidentDetailViewSerializer, CommentViewSerializer
from .models import ItsmIncidents, Comments

from rest_framework.views import APIView

class IncidentsViewSet(viewsets.ModelViewSet):
    queryset = ItsmIncidents.objects.all().order_by('platform_inc_number')
    serializer_class = ItsmIncidentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentCreateView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer_class = CommentSCreateSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
        return Response(status=201)

class CommentGetView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentViewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer_class = CommentViewSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
        return Response(status=200)



class IncidentDetailView(viewsets.ModelViewSet):
    def get(self, request, pk):
        incident = ItsmIncidents.objects.get(id=pk)
        serializer = IncidentDetailViewSerializer(incident)
        return  Response(serializer.data)
