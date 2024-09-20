from django.urls import path
from .views import Home, Register, Signin, Dashboard, Register2, Membership_card, Announcement, Linked, MembersReactivation, MembersModification, MembershipCard, Attendance, Events, Transactions, Products, ClearanceStatus, Archive, Reports, Settings, Index
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("register", Register.as_view(), name="Register"),
    path("signin", Signin.as_view(), name="Signin"),
    path("dashboard", Dashboard.as_view(), name="Dashboard"),
    path("register2", Register2.as_view(), name="Register2"),
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
    path("settings", Settings.as_view(), name="Settings"),
    
    path('index/', views.Index, name='Index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


