from django.urls import path
from .views import Home, Register, Signin, Announcement, Linked, MembersReactivation, MembersModification, MembershipCard, Attendance, Events, Transactions, Products, ClearancePage1, Archive, Reports, Settings, Dashboard, ClearancePage2, ClearancePage3
urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="Register"),
    path("signin", Signin.as_view(), name="Signin"),
    path("linked", Linked.as_view(), name="Linked"),
    path("members_reactivation", MembersReactivation.as_view(), name="MembersReactivation"),
    path("members_modification", MembersModification.as_view(), name="MembersModification"),
    path("membershipcard", MembershipCard.as_view(), name="MembershipCard"),
    path("attendance", Attendance.as_view(), name="Attendance"),
    path("events", Events.as_view(), name="Events"),
    path("transactions", Transactions.as_view(), name="Transactions"),
    path("products", Products.as_view(), name="Products"),
    path("clearance_page1", ClearancePage1.as_view(), name="ClearancePage1"),
    path("archive", Archive.as_view(), name="Archive"),
    path("reports", Reports.as_view(), name="Reports"),
    path("settings", Settings.as_view(), name="Settings"),
    path("create_announcement", Announcement.as_view(), name="CreateAnnouncement"),
    path("dashboard", Dashboard.as_view(), name="Dashboard"),
    path("clearance_page2", ClearancePage2.as_view(), name="ClearancePage2"),
    path("clearance_page3", ClearancePage3.as_view(), name="ClearancePage3")
]
