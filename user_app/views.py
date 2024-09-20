from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "user_app/home.html"

class Register(TemplateView):
    template_name = "registration/register.html"

class Register2(TemplateView):
    template_name = "registration/register2.html"

class Signin(TemplateView):
    template_name = "registration/signin.html"

class Dashboard(TemplateView):
    template_name = "user_app/dashboard.html"


def Index(request):
    return render(request, 'user_app/index.html')


class Membership_card(TemplateView):
    template_name = "user_app/membership_card.html"


class Announcement(TemplateView):
    template_name = "user_app/announcement.html"

class Linked(TemplateView):
    template_name = "user_app/linked.html"

class MembersReactivation(TemplateView):
    template_name = "user_app/members_reactivation.html"

class MembersModification(TemplateView):
    template_name = "user_app/members_modification.html"

class MembershipCard(TemplateView):
    template_name ="user_app/membershipcard.html"

class Attendance(TemplateView):
    template_name = "user_app/attendance.html"

class Events(TemplateView):
    template_name ="user_app/events.html"

class Transactions(TemplateView):
    template_name = "user_app/transaction.html"

class Products(TemplateView):
    template_name ="user_app/products.html"

class ClearanceStatus(TemplateView):
    template_name = "user_app/clearance_status.html"

class Archive(TemplateView):
    template_name ="user_app/archive.html"

class Reports(TemplateView):
    template_name ="user_app/reports.html"

class Settings(TemplateView):
    template_name ="user_app/settings.html"
