from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MyUsers, Albums
from .serializer import UserSerializer, AlbumSerializer
from rest_framework.generics import get_object_or_404


class UserView(APIView):
    def get(self, request):
        users = MyUsers.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        user = request.data.get('users')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User {} created successfully".format(user_saved.first_name)})

    def put(self, request, api_key):
        saved_user = get_object_or_404(MyUsers.objects.all(), api_key=api_key)
        data = request.data.get('users')
        print(data)
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()

        return Response({
            "success": "User {} updated successfully".format(user_saved.first_name)
        })

    def delete(self, request, api_key):
        user = get_object_or_404(MyUsers.objects.all(), api_key=api_key)
        serializer = UserSerializer(instance=user, data={'is_active': False}, partial=True)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

        return Response({
            "success": "User {} deleted successfully".format(user.first_name)
        })


class AlbumView(APIView):
    def get(self, request):
        albums = Albums.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response({'albums': serializer.data})

    def post(self, request):
        album = request.data.get('albums')
        # user = get_object_or_404(MyUsers.objects.all(), email=album.get('user_id'))
        user = MyUsers.objects.filter(email=album.get('user_id'))
        album.update({'user_id': user})
        serializer = AlbumSerializer(data=album)
        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({"success": "Album {} created successfully".format(album_saved.name)})