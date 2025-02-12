from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    """
    Represents a message sent from one user to another.
    """
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the message.
        Format: "Sender to Receiver: Message"
        """
        return f'{self.sender.username} to {self.receiver.username}: {self.message}'

class Profile(models.Model):
    """
    Represents additional information about a user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.
        Format: "Username's Profile"
        """
        return f"{self.user.username}'s Profile"