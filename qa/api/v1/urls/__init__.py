from .questionsurls import urlpatterns as questions_urls
from .answerurl import urlpatterns as answers_urls

urlpatterns = questions_urls + answers_urls