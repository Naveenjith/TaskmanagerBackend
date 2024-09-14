from rest_framework import generics
from .models import Task
from .serializers import Taskserializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.
class Listcreateview(generics.ListCreateAPIView): #list & create
    queryset=Task.objects.all()
    serializer_class=Taskserializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        status = self.request.query_params.get('status')
        queryset = Task.objects.filter(user=self.request.user)
        if status is not None:
            if status.lower() == 'completed':
                queryset = queryset.filter(status=True)
            elif status.lower() == 'pending':
                queryset = queryset.filter(status=False)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user to the current logged-in user

class Taskdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=Taskserializer
    permission_classes=[IsAuthenticated]

class Register(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [] 