from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Sequence, SubFactory
from factory.fuzzy import FuzzyText

from tracker.site.models import Project, Ticket


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


class TicketFactory(DjangoModelFactory):
    class Meta:
        model = Ticket

    title = Sequence(lambda n: u'title#%s' % n)
    description = FuzzyText()
    project = SubFactory(ProjectFactory)
    created_by = SubFactory(UserFactory)
