from django.contrib.auth.models import User
from django.test import TestCase

from .models import Dislikes, Likes, Profile, ViewHistory


class ProfileModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(
            user=user,
            full_name="Test User",
            gender="Male",
            age=25,
            city="Test City",
            hobbies="Reading, Coding",
            status="Searching",
            gallery=[],
            likes_count=0,
            privacy_settings={},
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.full_name, "Test User")
        self.assertEqual(self.profile.age, 25)


class ViewHistoryModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="viewer", password="pass1")
        user2 = User.objects.create(username="viewed", password="pass2")
        self.viewer_profile = Profile.objects.create(
            user=user1,
            full_name="Viewer",
            gender="Female",
            age=30,
            city="Viewer City",
            hobbies="Watching Movies",
            status="Searching",
            gallery=[],
            likes_count=0,
        )
        self.viewed_profile = Profile.objects.create(
            user=user2,
            full_name="Viewed",
            gender="Male",
            age=28,
            city="Viewed City",
            hobbies="Traveling",
            status="Searching",
            gallery=[],
            likes_count=0,
        )
        self.view_history = ViewHistory.objects.create(
            viewer=self.viewer_profile, viewed_profile=self.viewed_profile
        )

    def test_view_history_creation(self):
        self.assertEqual(self.view_history.viewer, self.viewer_profile)
        self.assertEqual(self.view_history.viewed_profile, self.viewed_profile)


class ApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = Profile.objects.create(
            user=self.user,
            full_name="Test User",
            gender="Male",
            age=25,
            city="Test City",
            hobbies="Reading",
            status="Searching",
            gallery=[],
            likes_count=0,
            privacy_settings={},
        )

    def test_profile_creation_api(self):
        response = self.client.post(
            "/api/profiles/",
            {
                "full_name": "New User",
                "gender": "Female",
                "age": 22,
                "city": "New City",
                "hobbies": "Gaming",
                "status": "Searching",
                "gallery": [],
                "likes_count": 0,
                "privacy_settings": {},
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Profile.objects.count(), 2)

    def test_view_history_api(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            "/api/view-history/",
            {
                "viewer": self.profile.id,
                "viewed_profile": self.profile.id,
            },
        )
        self.assertEqual(response.status_code, 201)


class ProfileModelTest(TestCase):
    def setUp(self):
        self.profile1 = Profile.objects.create(
            name="John Doe", age=30, bio="Profile John"
        )
        self.profile2 = Profile.objects.create(
            name="Jane Smith", age=25, bio="Profile Jane"
        )


class ViewHistoryModelTest(ProfileModelTest):
    def setUp(self):
        super().setUp()  # Вызываем setUp родительского класса
        self.view_history = ViewHistory.objects.create(
            viewer=self.profile1, viewed_profile=self.profile2
        )

    def test_view_history_creation(self):
        self.assertEqual(self.view_history.viewer, self.profile1)
        self.assertEqual(self.view_history.viewed_profile, self.profile2)
        self.assertIsNotNone(self.view_history.timestamp)


class LikesModelTest(ProfileModelTest):
    def setUp(self):
        super().setUp()
        self.like = Likes.objects.create(
            liker=self.profile1, liked_profile=self.profile2
        )

    def test_likes_creation(self):
        self.assertEqual(self.like.liker, self.profile1)
        self.assertEqual(self.like.liked_profile, self.profile2)
        self.assertIsNotNone(self.like.timestamp)


class DislikesModelTest(ProfileModelTest):
    def setUp(self):
        super().setUp()
        self.dislike = Dislikes.objects.create(
            disliker=self.profile1, disliked_profile=self.profile2
        )

    def test_dislikes_creation(self):
        self.assertEqual(self.dislike.disliker, self.profile1)
        self.assertEqual(self.dislike.disliked_profile, self.profile2)
        self.assertIsNotNone(self.dislike.timestamp)
