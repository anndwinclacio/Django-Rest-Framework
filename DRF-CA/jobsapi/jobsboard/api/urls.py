from django.urls import path 
from jobsboard.api.views import JobListCreateAPIView, JobDetailAPIView

urlpatterns = [
    path("jobs/", JobListCreateAPIView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobDetailAPIView.as_view(), name="job-detail")
]