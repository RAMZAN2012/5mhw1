from rest_framework.views import APIView
from rest_framework.response import Response
from apps.api.models import Task
from apps.api.serializers import PostSerializer

class PostListAPView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = PostSerializer(tasks, many=True)
        return Response(serializer.data)
