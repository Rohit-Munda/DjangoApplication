from django.db import models
from datetime import time


class Room(models.Model):
    room_no = models.IntegerField()
    floor_no = models.IntegerField()
    room_name = models.CharField(max_length=200)

    def __str__(self):
        return f"Room {self.room_no} is named {self.room_name} at floor {self.floor_no}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
