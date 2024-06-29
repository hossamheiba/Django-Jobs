from django.urls import path
from . import views
# from .import api

app_name="job"

urlpatterns = [
    path("home_page",views.home_page,name="home_page"),
    path("job_list",views.job_list,name="job_list"),
    path("add_job",views.add_jobs,name="add_job"),
    path("<str:slug>",views.job_detail,name="job_detail"),

    #API
    # path("api/list",api.API.as_view(),name="api"),
    # path("api/list/<str:slug>",api.API_detail.as_view(),name="api-detail"),
       
]
