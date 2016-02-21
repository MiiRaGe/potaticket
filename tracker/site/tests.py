from djangae.test import TestCase
from django.http import Http404
from django.template import TemplateSyntaxError
from django.test import RequestFactory
from django_webtest import WebTest

from tracker.site.models import Ticket
from tracker.site.views import update_project_view, update_ticket_view, create_ticket_view, delete_ticket_view
from tracker.site.factories import ProjectFactory, TicketFactory


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


class TicketTest(TestCase):
    def setUp(self):
        self.ticket = TicketFactory.create()
        self.user = self.ticket.created_by
        self.project = self.ticket.project
        self.rf = RequestFactory()

    def test_switch_ticket_ownership(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        project2 = ProjectFactory.create()
        self.assertNotEqual(project2.id, self.project.id)

        request = self.rf.get('/projects/%s/tickets/%s/edit' % (project2.id, self.ticket.id))
        request.user = self.user
        self.assertRaises(Http404, update_ticket_view, request, project_id=project2.id, ticket_id=self.ticket.id)

    def test_ticket_edit(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.get('/projects/%s/tickets/%s/edit' % (self.project.id, self.ticket.id))
        request.user = self.user
        r = update_ticket_view(request, project_id=self.project.id, ticket_id=self.ticket.id)
        self.assertEqual(r.status_code, 200)
        r.render()
        self.assertIn(u'Submit', r.content.decode('utf8'))

    def test_ticket_delete(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.post('/projects/%s/tickets/%s/delete' % (self.project.id, self.ticket.id))
        request.user = self.user
        r = delete_ticket_view(request, project_id=self.project.id, ticket_id=self.ticket.id)
        self.assertEqual(r.status_code, 302)
        self.assertFalse(Ticket.objects.filter(id=self.ticket.id).exists())


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
