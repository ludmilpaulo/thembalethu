from django.urls import path
from .views import CarouselListCreateView, AboutUsListCreateView, TeamListCreateView, ContactListCreateView, ClientCreateView

urlpatterns = [
    path('carousel/', CarouselListCreateView.as_view(), name='carousel-list-create'),
    path('about-us/', AboutUsListCreateView.as_view(), name='aboutus-list-create'),
    path('team/', TeamListCreateView.as_view(), name='team-list-create'),
    path('contact/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('clients/', ClientCreateView.as_view(), name='client-list'),
]
