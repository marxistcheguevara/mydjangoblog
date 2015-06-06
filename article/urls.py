from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^all/$', 'article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
	#url(r'^cat/(?P<category_id>\d+)/$', 'article.views.category'),
	#url(r'^author/(?P<author_id>\d+)/$', 'article.views.author'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
    url(r'^create/$',  'article.views.create'), 
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'), 
    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
    url(r'^search/$', 'article.views.search_titles'),
  # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
