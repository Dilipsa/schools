from django.urls import path
from . import views

app_name="core"
urlpatterns = [
    path("giver/", views.GiverView.as_view(), name="giver"),
    path("giver-detail/<int:pk>/", views.GiverDetailView.as_view(), name="giver_detail"),
    path("history/", views.HistoryView.as_view(), name="history"),
    path("about/", views.AboutUsView.as_view(), name="about"),
    path("taker/", views.TakerView.as_view(), name="taker"),
    path("faq/", views.FAQView.as_view(), name="faq"),
    path("mission/", views.MissionView.as_view(), name="mission"),
    path("vision/", views.VisionView.as_view(), name="vision"),
    path("phone/", views.PhoneView.as_view(), name="phone"),
    path("feedback/", views.FeedBackView.as_view(), name="feedback"),

    path("admin-taker/", views.TakerListView.as_view(), name="admin_taker"),
    path("admin-approve/<int:pk>/", views.approval_view, name="admin_approve"),
    path("admin-unapprove/<int:pk>/", views.unapproval_view, name="admin_unapprove"),
    path("donate/<str:username>/<int:pk>/", views.donate_view, name="donate"),
    path("volunteer/<str:username>/<int:pk>/", views.volunteer, name="volunteer"),
    path("volunteer-list/", views.volunteer_list_view, name="volunteer_list"),
    path("donation-history/", views.donation_history, name="donation_history"),
    path("feedback/<int:pk>/", views.feedback_view, name="feedback"),
]