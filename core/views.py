from django.http import FileResponse
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import ReportSerializer, UserSerializer
from .reports import generate_report


class UserListView(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReportView(APIView):
    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = [
            [f.name for f in User._meta.fields],
            *User.objects.all().values_list(),
        ]
        buffer, content_type, filename = generate_report(
            data, serializer.data["file_type"]
        )
        buffer.seek(0)
        return FileResponse(buffer, content_type=content_type, filename=filename)
