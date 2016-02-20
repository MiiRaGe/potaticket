from djangae.test import TestCase
from django.template import TemplateSyntaxError
from django.test import RequestFactory
from django_webtest import WebTest

from tracker.site.views import update_project_view, create_ticket_view
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
        self.assertEqual(r.status_code, 200)
        try:
            r.render()
        except TemplateSyntaxError:
            raise AssertionError('Template cannot render properly')
        self.assertIn(u'Edit', r.content.decode('utf8'))

    def test_project_create_ticket(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.get('/projects/%s/tickets/create' % self.project.id)
        request.user = self.user
        r = create_ticket_view(request, project_id=self.project.id)
        self.assertEqual(r.status_code, 200)
        try:
            r.render()
        except TemplateSyntaxError:
            raise AssertionError('Template cannot render properly')
        self.assertIn(u'Submit', r.content.decode('utf8'))


class ProjectWebTest(WebTest):
    def setUp(self):
        self.project = ProjectFactory.create()
        self.user = self.project.created_by

    def test_project_details(self):
        projects_list = self.app.get('/projects/', user=self.user.username)
        self.assertIn(self.project.title, projects_list)

        # Now click on the title to access details
        try:
            project_details = projects_list.click(self.project.title)
        except IndexError:
            raise AssertionError('%s is not a clickable link in the page' % self.project.title)
        # Not ideal as using string which can change.
        self.assertIn('Create ticket', project_details)
