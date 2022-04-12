from django.shortcuts import render, get_object_or_404
import logging
from django.shortcuts import redirect
from blog.forms import CommentForm
# Create your views here.
logger = logging.getLogger(__name__)
def index(request):
  
  return render(request, "blog/index.html")
  logger.debug("Got %d posts", len(posts))
  logger.info(
    "Created comment on Post %d for user %s", post.pk, request.user
  )
def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  if request.user.is_active:
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = post
            comment.creator = request.user
            comment.save()
            return redirect(request.path_info)
    else:
        comment_form = CommentForm()
  else:
      comment_form = None
  return render(
    request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
  )