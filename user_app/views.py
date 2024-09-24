from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class Register(TemplateView):
    template_name = "pages/register.html"

class Sign_in(TemplateView):
    template_name = "pages/sign_in.html"

class Linked(TemplateView):
    template_name = "pages/linked.html"

class o_reactivate_member(TemplateView):
    template_name = "pages/o_reactivate_member.html"

class MembersModification(TemplateView):
    template_name = "pages/members_modification.html"

class MembershipCard(TemplateView):
    template_name ="pages/membershipcard.html"

class o_attendance(TemplateView):
    template_name = "pages/o_attendance.html"

class Events(TemplateView):
    template_name ="pages/events.html"

class Transactions(TemplateView):
    template_name = "pages/transaction.html"

class Products(TemplateView):
    template_name ="pages/products.html"

class o_clearance_clearance(TemplateView):
    template_name = "pages/o_clearance_rec_clearance.html"

class Archive(TemplateView):
    template_name ="pages/archive.html"

class Reports(TemplateView):
    template_name ="pages/reports.html"

class Settings(TemplateView):
    template_name ="pages/settings.html"

class Announcement(TemplateView):
    template_name ="pages/create_announcements.html"

class Dashboard(TemplateView):
    template_name ="pages/o_dashboard.html"

class o_clearance_rec_processing(TemplateView):
    template_name ="pages/o_clearance_rec_processing.html"

class o_clearance_rec_requirements(TemplateView):
    template_name ="pages/o_clearance_rec_requirements.html"

class o_attendance_add(TemplateView):
    template_name ="pages/o_attendance_add.html"
