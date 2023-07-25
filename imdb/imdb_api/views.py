from django.http import HttpResponse, JsonResponse, Http404
from .models import Watchlist, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('watchlist-list', request=request, format=format),
        'streamplatform': reverse('streamplatform-list', request=request, format=format),
    })

class ReviewCreateView(generics.CreateAPIView):

    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk= self.kwargs['pk']
        movie = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=movie)


class ReviewListView(generics.ListAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class StreamPlatformViewSet(viewsets.ModelViewSet):

    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class WatchListViewSet(viewsets.ModelViewSet):

    queryset = Watchlist.objects.all()
    serializer_class = WatchListSerializer

# class StreamPlatformList(generics.ListCreateAPIView):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

# class StreamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer


# ***************** mixins ******************
# class StreamPlatformList(mixins.ListModelMixin, 
#                         mixins.CreateModelMixin, 
#                         generics.GenericAPIView):

#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
        
#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args, **kwargs)


# class StreamPlatformDetail(mixins.RetrieveModelMixin,
#                            mixins.UpdateModelMixin,
#                            mixins.DestroyModelMixin,
#                            generics.GenericAPIView):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ************** class based views **************** 
# class StreamPlatformList(APIView):

#     def get(self, request, format=None):
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)
    
#     def post(self, request, format=None):
#         data = request.data 
#         serialized = StreamPlatformSerializer(data = data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# class StreamPlatformDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         stream_platform = self.get_object(pk)
#         serialized = StreamPlatformSerializer(stream_platform)
#         return Response(serialized.data)
    
#     def put(self, request, pk, format=None):
#         stream_platform = self.get_object(pk)
#         data = request.data
#         serialized = StreamPlatformSerializer(stream_platform, data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         stream_platform = self.get_object(pk)
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def movie_list(request):
    movielist = Watchlist.objects.all()
    serialized = WatchListSerializer(movielist, many=True)
    return Response(serialized.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Watchlist.objects.get(pk=pk)
    serialized = WatchListSerializer(movie)
    return Response(serialized.data)

# ******************* function based views *************
# # for list , post and get 
# @api_view(['GET', 'POST'])
# def stream_list(request, format=None):
#     if request.method == 'GET':
#         stream_list = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializer(stream_list, many=True)
#         return Response(serialized.data)

#     elif request.method == 'POST':
#         data = request.data 
#         serialized = StreamPlatformSerializer(data = data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


# # for one stream platform = put, get and delete
# @api_view(['PUT', 'GET', 'DELETE']) 
# def stream_detail(request, pk, format=None):
#     try:
#         stream_platform = StreamPlatform.objects.get(pk=pk)
#     except StreamPlatform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serialized = StreamPlatformSerializer(stream_platform)
#         return Response(serialized.data)
    
#     elif request.method == 'PUT':
#         data = request.data
#         serialized = StreamPlatformSerializer(stream_platform, data=data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         stream_platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
