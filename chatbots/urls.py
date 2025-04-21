from rest_framework.routers import DefaultRouter

from chatbots.views import index

app_name = 'chatbot'
api_router = DefaultRouter(trailing_slash=False)
api_router.register('', index.IndexViewSet, 'index')

urlpatterns = []
urlpatterns += api_router.urls
