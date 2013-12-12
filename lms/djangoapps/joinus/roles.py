from courseware.roles import AccessRole
from joinus.models import JoinUs


class JoinUsInstructor(AccessRole):
    def __init__(self, name):
        """An instructor in a JoinUs group"""
        self.name = name

    def has_user(self, user):  # pylint: disable=unused-argument
        """
        Return whether the supplied django user has access to this role.
        """
        return user in JoinUs.group(self.name).leaders

    def add_users(self, *users):
        """
        Add the role to the supplied django users.
        """
        JoinUs.group(self.name).leaders.add(*users)

    def remove_users(self, *users):
        """
        Remove the role from the supplied django users.
        """
        JoinUs.group(self.name).leaders.remove(*users)

    def users_with_role(self):
        """
        Return a django QuerySet for all of the users with this role
        """
        return JoinUs.group(self.name).leaders
