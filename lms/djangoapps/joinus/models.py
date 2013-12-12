from django.contrib.auth.models import User, Group
from django.db import models
from django.contrib.auth.decorators import permission_required

JOINUS_GROUP_PREFIX = "joinus_"

class JoinUs(models.Model):
	"""
	Models a user-created study group.
	"""
	name = models.CharField(max_length=255)
	members = models.ForeignKey(Group)
	leader = models.ForeignKey(User)

	@classmethod
	def join_joinus_group(cls, user, gname):
		""" Adds user to the JoinUs Group with name gname. """
		gname = JOINUS_GROUP_PREFIX + gname
		joinus_group = cls.objects.get(name='gname')
		joinus_group.members.user_set.add(user)
		joinus_group.save()
		return

	# Invite codes are future TODO; not in scope for datajam
	@classmethod
	def process_invite_code(cls, code, user):
		# if invite_code is valid
		# add_user_to_group
		# else, return error
		pass

	@classmethod
	def remove_user_from_joinus_group(cls, user, gname):
		""" 
		Removes user from the JoinUs Group with name gname.
		If that user is the group leader, this also deletes the group.
		"""
		gname = JOINUS_GROUP_PREFIX + gname
		joinus_group.cls.objects.get(name='gname')
		joinus_group.members.user_set.remove(user)
		joinus_group.save()
		# TODO if user is group leader, delete group
		return

	def get_joinus_group_info(self, user):
		# lets a user see the code they have access to
		pass

	@classmethod
	def create_joinus_group(cls, user, gname):
		# creates a new group led by user with name
		# TODO check that name is valid, not taken, etc
		gname = JOINUS_GROUP_PREFIX + gname
		group = Group()
		joinus_group = cls.objects.create(members=group, leader=user, name=gname)
		joinus_group.save()
		return
