from .authenticateurls import urlpatterns as auth_urls
from .skillurls import urlpatterns as skill_urls

urlpatterns = auth_urls + skill_urls
