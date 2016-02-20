from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Sequence, SubFactory

from tracker.site.models import Project


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = Sequence(lambda n: u'username#%s' % n)
    email = Sequence(lambda n: u'username%s@gmail.com' % n)
    first_name = Sequence(lambda n: u'first_name#%s' % n)
    last_name = Sequence(lambda n: u'last_name#%s' % n)


class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project

    title = Sequence(lambda n: u'title#%s' % n)
    created_by = SubFactory(UserFactory)
