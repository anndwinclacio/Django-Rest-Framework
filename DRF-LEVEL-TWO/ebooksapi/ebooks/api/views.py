from rest_framework import generics
from rest_framework import permissions     # so that our permission system can be modified in each view
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404


from ebooks.models import Ebook, Review
from ebooks.api.pagination import SmallSetPagination
from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


""" Concrete API View Class """
class EbookListCreateAPIView(generics.ListCreateAPIView): # if you are going to see the def, it is the same with the once declared below

    queryset = Ebook.objects.all().order_by("-id") # to prevent the warning made by the pagination class   
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Ebook.objects.all()    
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):    # since the models are connected, we need to override the function
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
      
        review_author = self.request.user

        # PERFORMING VALIDATION CHECK -so that only one review can be created by a single user.
        review_queryset = Review.objects.filter(ebook=ebook, 
                                                review_author=review_author)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this Ebook.")
      
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]



""" Generic API View Class """
# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):

#     queryset = Ebook.objects.all()    # imported from generics.GenericAPIView
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs) # imported from mixins
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)