from django.contrib.auth.models import User, Group
from django.db import models

JOINUS_GROUP_PREFIX = "joinus_"


class JoinUs(Group):
    """
    Models a user-created study group.
    """
    leaders = models.ManyToManyField(User)

    @classmethod
    def group_name(cls, name):
        return JOINUS_GROUP_PREFIX + name

    @property
    def display_name(self):
        return self.name[len(JOINUS_GROUP_PREFIX):]

    @classmethod
    def group(cls, name):
        return JoinUs.objects.get(name=cls.group_name(name))

    @classmethod
    def join_joinus_group(cls, user, gname):
        """ Adds user to the JoinUs Group with name gname. """
        cls.group(gname).user_set.add(user)

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
        cls.group(gname).user_set.remove(user)
        # TODO if user is group leader, delete group

    def get_joinus_group_info(self, user):
        # lets a user see the code they have access to
        pass

    @classmethod
    def create_joinus_group(cls, user, gname):
        # creates a new group led by user with name
        # TODO check that name is valid, not taken, etc
        joinus_group = cls(
            name=cls.group_name(gname)
        )
        joinus_group.save()
        joinus_group.leaders.add(user)

    @classmethod
    def is_student_led_by(student, leader):
        return JoinUs.objects.filter(user__contains=student_id, leaders__contains=request.user).exists()
