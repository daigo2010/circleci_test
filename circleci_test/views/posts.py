from django.template import Context, loader, RequestContext
from circleci_test.models import Posts
from django.http import HttpResponse
from datetime import datetime

def index(request):
    if request.method == "POST":
        p = Posts(name=request.POST['name'], description=request.POST['description'],url=request.POST['url'],  created_at=datetime.now())
        p.save()
    Posts
    posts = Posts.objects.all().order_by('-created_at')[:5]
    t = loader.get_template('./index.html')
    c = RequestContext(request, {
        'posts': posts,
    })

    return HttpResponse(t.render(c))
