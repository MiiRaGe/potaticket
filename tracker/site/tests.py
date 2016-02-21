from djangae.test import TestCase
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.template import TemplateSyntaxError
from django.test import RequestFactory, override_settings
from django_webtest import WebTest

from tracker.checks import check_csp_is_not_report_only, check_session_csrf_enabled
from tracker.site.models import Ticket, Project
from tracker.site.views import update_project_view, update_ticket_view, create_ticket_view, delete_ticket_view, \
    my_tickets_view, create_project_view
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

    def test_project_create_get(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.get('/projects/create')
        request.user = self.user
        r = create_project_view(request)
        self.assertEqual(r.status_code, 200)
        r.render()
        self.assertIn(u'Submit', r.content.decode('utf8'))

    def test_project_create_post(self):
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
        request = self.rf.post('/projects/create', data={'title': 'New project'})
        request.user = self.user
        r = create_project_view(request)
        self.assertEqual(r.status_code, 302)
        self.assertTrue(Project.objects.filter(title='New project'))


class TicketTest(TestCase):
    def setUp(self):
        self.ticket = TicketFactory.create()
        self.user = self.ticket.created_by
        self.project = self.ticket.project
        self.rf = RequestFactory()

    def test_my_tickets_not_authenticated(self):
        request = self.rf.get('/')
        request.user = AnonymousUser()
        r = my_tickets_view(request)
        self.assertEqual(r.status_code, 200)

    def test_my_tickets_authenticated(self):
        request = self.rf.get('/')
        request.user = self.user
        r = my_tickets_view(request)
        self.assertEqual(r.status_code, 200)

    def test_switch_ticket_ownership(self):
        project2 = ProjectFactory.create()
        self.assertNotEqual(project2.id, self.project.id)

        request = self.rf.get('/projects/%s/tickets/%s/edit' % (project2.id, self.ticket.id))
        # I'm unsure how to test with logged user using djangoae
        # Using request factory to bypass that.
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


class CheckTests(TestCase):
    @override_settings(MIDDLEWARE_CLASSES=[])
    def test_check_missing_session_middleware(self):
        self.assertEqual(check_session_csrf_enabled(), ['SESSION_CSRF_DISABLED'])

    @override_settings(CSP_REPORT_ONLY=True)
    def test_check_missing_csp_report_only_setting(self):
        self.assertEqual(check_csp_is_not_report_only(), ['CSP_REPORT_ONLY_ENABLED'])

    @override_settings(MIDDLEWARE_CLASSES=['session_csrf.CsrfMiddleware'])
    def test_check_middleware_csrf_is_present(self):
        self.assertEqual(check_session_csrf_enabled(), [])

    @override_settings(CSP_REPORT_ONLY=False)
    def test_check_csp_report_is_missing(self):
        self.assertEqual(check_csp_is_not_report_only(), [])
