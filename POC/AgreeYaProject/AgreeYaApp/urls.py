from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("data", views.data, name="data"),
    path("scrub/upload/", views.upload_crub_data, name="file_upload"),
    path("scrub/get_csv_headers/", views.get_csv_headers, name="csv_headers"),
    path("scrub/headers/data/", views.scrub_headers_data, name="scrub_headers_data"),
    path("scrub/download/", views.download_file, name="download_file")
    ]