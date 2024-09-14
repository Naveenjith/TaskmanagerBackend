from rest_framework import generics
from .models import Task
from .serializers import Taskserializer,Userserializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.
class Listcreateview(generics.ListCreateAPIView): #list & create
    queryset=Task.objects.all()
    serializer_class=Taskserializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.data)  # Log the incoming request data
        serializer.save()

        
    def get_queryset(self):
        status=self.request.query_params.get('status')
        queryset=Task.objects.all()
        if status is not None:
            if status.lower()=='completed':
                queryset=queryset.filter(status=True)
            elif status.lower()=='pending':
                queryset=queryset.filter(status=False)
        return queryset

class Taskdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=Taskserializer
    permission_classes=[IsAuthenticated]

class Register(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer