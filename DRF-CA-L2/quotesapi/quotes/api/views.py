from rest_framework import generics
from rest_framework import permissions

from quotes.models import Quote 
from quotes.api.pagination import SmallSetPagination
from quotes.api.permissions import IsAdminUserOrReadOnly
from quotes.api.serializers import QuoteSerializer

class QuoteListCreateAPIView(generics.ListCreateAPIView): 

    queryset = Quote.objects.all().order_by("id") 
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Quote.objects.all()    
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]