# views.py
from rest_framework import generics
from .models import Carousel, AboutUs, Team, Contact, Client
from .serializers import CarouselSerializer, AboutUsSerializer, TeamSerializer, ContactSerializer, ClientSerializer

class CarouselListCreateView(generics.ListCreateAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class AboutUsListCreateView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ClientCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
