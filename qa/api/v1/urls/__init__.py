from .questionsurls import urlpatterns as questions_urls
from .answerurl import urlpatterns as answers_urls
from .vote_urls import urlpatterns as vote_urls

urlpatterns = questions_urls + answers_urls + vote_urls