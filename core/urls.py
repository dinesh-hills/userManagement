from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register("usercreate", views.UserListView, basename="users")

urlpatterns = [
    path("report_type/", views.ReportView.as_view(), name="reports"),
] + router.urls
