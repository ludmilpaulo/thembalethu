from rest_framework import serializers
from .models import Carousel, AboutUs, Team, Contact, Client

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ['title', 'content', 'logo', 'client', 'logo_url']

    def get_logo_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
