from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Room
from polls.forms import ResponseForm

class RoomTests(TestCase):
	def test_room_name(self):
		"""The given name of a room should match a string of that name."""
		test_room = Room.objects.create(name="Test Room", description="Test description.", 
		dictionary={'yes': 'next-room'}, slug="test-room")
		self.assertEqual(Room.objects.get(name="Test Room").name, "Test Room")
	
	def test_room_description(self):
		"""The given description of a room should match a string of that description."""
		test_room = Room.objects.create(name="Test Room", description="Test description.", 
		dictionary={'yes': 'next-room'}, slug="test-room")
		self.assertEqual(Room.objects.get(name="Test Room").description, "Test description.")

	def test_room_dictionary(self):
		"""The given dictionary of a test room should contain a key in that dictionary."""
		test_room = Room.objects.create(name="Test Room", description="Test description.", 
		dictionary={'yes': 'next-room', 'no': 'other-room', 'maybe': 'third-room'}, slug="test-room")
		self.assertEqual(Room.objects.get(name="Test Room").dictionary['no'], "other-room")
		
	def test_room_slug(self):
		"""The given slug of a room should match a string of that slug."""
		test_room = Room.objects.create(name="Test Room", description="Test description.", 
		dictionary={'yes': 'next-room'}, slug="test-room")
		self.assertEqual(Room.objects.get(name="Test Room").slug, "test-room")
										

	
	