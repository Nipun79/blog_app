from django.urls import path
from . views import CreateEntryView, EntryView, HomeView
urlpatterns = [
    path('',HomeView.as_view(),name="blog-name"),
    path('entry/<int:pk>/',EntryView.as_view(),name="entry-name"),
    path('create_entry/',CreateEntryView.as_view(success_url="/"),name="create-entry")
]
