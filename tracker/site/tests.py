from djangae.test import TestCase
from django.template import TemplateSyntaxError
from django.test import RequestFactory

from tracker.site.views import update_project_view
from tracker.site.factories import ProjectFactory


class ProjectTest(TestCase):
    def setUp(self):
        self.project = ProjectFactory.create()
        self.user = self.project.created_by
        self.rf = RequestFactory()

    def test_project_edit(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.get('/projects/%s/edit/' % self.project.id)
        request.user = self.user
        r = update_project_view(request, project_id=self.project.id)
        assert r.status_code == 200
        try:
            r.render()
        except TemplateSyntaxError:
            raise AssertionError('Template cannot render properly')
        assert u'Edit' in r.content