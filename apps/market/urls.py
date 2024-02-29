from django.urls import path
from apps.market.views import *

app_name = 'market'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('author-detail-page/<pk>', AuthorDetailPageView.as_view(), name='author-detail'),
    path('authors-page/', AuthorsPage.as_view(), name='authors'),
    path('details-page/<pk>', ProductDetailPageView.as_view(), name='details'),
    path('create-page/', ProductCreatePageView.as_view(), name='create'),
    path('explore-page/', ExplorePageView.as_view(), name='explore'),
    path('explore-authors/<pk>', ExploreAuthorView.as_view(), name='explore-author'),
    path('explore-categories/<pk>', ExploreCategoriyView.as_view(), name='explore-categoriy'),
    path('explore-likes/<pk>', author_like, name='like'), 
    path('details-page-add-card/<pk>', AddToCardAuthor.as_view(), name='author-card'), 
]
