"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import MatchEntry.views as meViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entry/questions', meViews.allQuestions),
    path('entry/create', meViews.createEntry),
    path('entry/get', meViews.retrieveUser),
    path("entry/assign_opps", meViews.assign_opps, name="assign_opps"),
    path("entry/engagement_email", meViews.sendEngagementEmail, name="engagement_email"),
    path("entry/update_email", meViews.sendUpdateEmail, name="update_email"),
    path("entry/result_email", meViews.sendResultEmail, name="result_email"),
]
