from django.urls import include, path
from rest_framework.routers import DefaultRouter
from attached_files.views import AttachedFileViewSet

app_name = "attached_files"

router = DefaultRouter()
router.register("files", AttachedFileViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
