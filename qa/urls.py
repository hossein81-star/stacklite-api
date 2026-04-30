from django.urls import path, include

app_name = 'qa'

urlpatterns = [
    path('api/v1/', include('qa.api.v1.urls'),),
]