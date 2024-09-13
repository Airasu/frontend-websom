from django.urls import path
from .views import Home, Register, Signin, Announcement, Linked, MembersReactivation, MembersModification, MembershipCard, Attendance, Events, Transactions, Products, ClearanceStatus, Archive, Reports, Settings

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="Register"),
    path("signin", Signin.as_view(), name="Signin"),
    path("announcement", Announcement.as_view(), name="Announcement"),
    path("linked", Linked.as_view(), name="Linked"),
    path("members_reactivation", MembersReactivation.as_view(), name="MembersReactivation"),
    path("members_modification", MembersModification.as_view(), name="MembersModification"),
    path("membershipcard", MembershipCard.as_view(), name="MembershipCard"),
    path("attendance", Attendance.as_view(), name="Attendance"),
    path("events", Events.as_view(), name="Events"),
    path("transactions", Transactions.as_view(), name="Transactions"),
    path("products", Products.as_view(), name="Products"),
    path("clearance_status", ClearanceStatus.as_view(), name="ClearanceStatus"),
    path("archive", Archive.as_view(), name="Archive"),
    path("reports", Reports.as_view(), name="Reports"),
    path("settings", Settings.as_view(), name="Settings")
]
