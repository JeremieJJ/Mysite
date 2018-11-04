from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
            url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="blog/post.html")),
			url(r'^blog/wood/$', views.wood, name='wood'),
			url(r'^blog/jet_impact/$', views.jet_impact, name='jet_impact'),
			url(r'^blog/MCP/$', views.MCP, name='MCP'),
            ]
			
