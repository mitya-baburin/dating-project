from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Dislikes, Likes, Profile, ViewHistory
from .serializers import ProfileSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])  # Ограничиваем доступ
def profile_list(request):
    if request.method == "GET":
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_profile(request):
    user = request.user.profile
    profile_id = request.data.get("profile_id")
    profile_to_like = Profile.objects.get(id=profile_id)

    if not Likes.objects.filter(user=user, liked_profile=profile_to_like).exists():
        Likes.objects.create(user=user, liked_profile=profile_to_like)
        return Response({"message": "Profile liked"}, status=status.HTTP_201_CREATED)

    return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def dislike_profile(request):
    user = request.user.profile
    profile_id = request.data.get("profile_id")
    profile_to_dislike = Profile.objects.get(id=profile_id)

    if not Dislikes.objects.filter(
        user=user, disliked_profile=profile_to_dislike
    ).exists():
        Dislikes.objects.create(user=user, disliked_profile=profile_to_dislike)
        return Response({"message": "Profile disliked"}, status=status.HTTP_201_CREATED)

    return Response({"message": "Already disliked"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def view_profile(request):
    viewer = request.user.profile
    profile_id = request.data.get("profile_id")
    viewed_profile = Profile.objects.get(id=profile_id)

    ViewHistory.objects.create(viewer=viewer, viewed_profile=viewed_profile)
    return Response({"message": "Profile viewed"}, status=status.HTTP_201_CREATED)
