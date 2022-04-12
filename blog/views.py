from django.shortcuts import render
import logging
# Create your views here.
logger = logging.getLogger(__name__)
def index(request):
  
  return render(request, "blog/index.html")
  logger.debug("Got %d posts", len(posts))
  logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
  )