from django.urls import path
from .views import Home, Register, Sign_in, Announcement, Linked, o_reactivate_member, MembersModification, MembershipCard, o_attendance, Events, Transactions, Products, o_clearance_clearance, Archive, Reports, Settings, Dashboard, o_clearance_rec_processing, o_clearance_rec_requirements, o_attendance_add
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="register"),
    path("sign_in", Sign_in.as_view(), name="sign_in"),
    path("linked", Linked.as_view(), name="Linked"),
    path("o_reactivate_member", o_reactivate_member.as_view(), name="o_reactivate_member"),
    path("members_modification", MembersModification.as_view(), name="MembersModification"),
    path("membershipcard", MembershipCard.as_view(), name="MembershipCard"),
    path("o_attendance", o_attendance.as_view(), name="o_attendance"),
    path("events", Events.as_view(), name="Events"),
    path("transactions", Transactions.as_view(), name="Transactions"),
    path("products", Products.as_view(), name="Products"),
    path("o_clearance_clearance", o_clearance_clearance.as_view(), name="o_clearance_clearance"),
    path("archive", Archive.as_view(), name="Archive"),
    path("reports", Reports.as_view(), name="Reports"),
    path("settings", Settings.as_view(), name="Settings"),
    path("create_announcement", Announcement.as_view(), name="CreateAnnouncement"),
    path("o_dashboard", Dashboard.as_view(), name="o_dashboard"),
    path("o_clearance_rec_processing", o_clearance_rec_processing.as_view(), name="o_clearance_rec_processing"),
    path("o_clearance_rec_requirements", o_clearance_rec_requirements.as_view(), name="o_clearance_rec_requirements"),
    path("o_attendance_add", o_attendance_add.as_view(), name="o_attendance_add")
]
