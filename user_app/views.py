from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class Register(TemplateView):
    template_name = "pages/register.html"

class Register2(TemplateView):
    template_name = "pages/register2.html"

class Signin(TemplateView):
    template_name = "pages/signin.html"

class Dashboard(TemplateView):
    template_name = "pages/dashboard.html"


def Index(request):
    return render(request, 'pages/index.html')


class Membership_card(TemplateView):
    template_name = "pages/membership_card.html"


class Announcement(TemplateView):
    template_name = "pages/announcement.html"

class Linked(TemplateView):
    template_name = "pages/linked.html"

class MembersReactivation(TemplateView):
    template_name = "pages/members_reactivation.html"

class MembersModification(TemplateView):
    template_name = "pages/members_modification.html"

class MembershipCard(TemplateView):
    template_name ="pages/membershipcard.html"

class Attendance(TemplateView):
    template_name = "pages/attendance.html"

class Events(TemplateView):
    template_name ="pages/events.html"

class Transactions(TemplateView):
    template_name = "pages/transaction.html"

class Products(TemplateView):
    template_name ="pages/products.html"

class ClearanceStatus(TemplateView):
    template_name = "pages/clearance_status.html"

class Archive(TemplateView):
    template_name ="pages/archive.html"

class Reports(TemplateView):
    template_name ="pages/reports.html"

class Settings(TemplateView):
    template_name ="pages/settings.html"
