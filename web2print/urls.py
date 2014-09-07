from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web2print.views.home', name='home'),
    url(r'^/*', include("core.urls")),
    url(r'^/*', include("banner.urls")),
    url(r'^/*', include("article_category.backend_urls")),
    url(r'^/*', include("article.backend_urls")),
    url(r'^/*', include("paper_category.backend_urls")),
    url(r'^/*', include("service_category.backend_urls")),
    url(r'^/*', include("service.backend_urls")),
    url(r'^/*', include("product_format.backend_urls")),
    url(r'^/*', include("paper_type.backend_urls")),
    url(r'^/*', include("product_category.backend_urls")),
    url(r'^/*', include("product_subcategory.backend_urls")),
    url(r'^/*', include("product.backend_urls")),
    url(r'^/*', include("article.frontend_urls")),
    url(r'^/*', include("user.frontend_urls")),
    url(r'^/*', include("product.frontend_urls")),
    url(r'^/*', include("product_subcategory.frontend_urls")),
    url(r'^/*', include("product_category.frontend_urls")),
    url(r'^$', 'frontpage.views.index', name="index-page"),
)
