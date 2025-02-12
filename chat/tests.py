from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message

class ChatTests(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(username='user1', password='testpass123')
        self.user2 = User.objects.create_user(username='user2', password='testpass123')

        # Create a test message
        self.message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            message='Hello, User 2!'
        )

        # Initialize the test client
        self.client = Client()

    def test_chat_home_view(self):
        # Log in as user1
        self.client.login(username='user1', password='testpass123')

        # Access the chat home page
        response = self.client.get(reverse('chat_home'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_chat_room_view(self):
        # Log in as user1
        self.client.login(username='user1', password='testpass123')

        # Access the chat room with user2
        response = self.client.get(reverse('chat_room', args=[self.user2.id]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_message_creation(self):
        # Check that the test message was created correctly
        self.assertEqual(self.message.message, 'Hello, User 2!')
        self.assertEqual(self.message.sender.username, 'user1')
        self.assertEqual(self.message.receiver.username, 'user2')