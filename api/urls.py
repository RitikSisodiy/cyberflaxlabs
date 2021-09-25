from rest_framework.routers import DefaultRouter
from . import views as apiviews
#creating router object
router = DefaultRouter()
router.register('ourworkcat',apiviews.ourWork_catModelViewset,basename='ourwork')
router.register('ourcatbanner',apiviews.headbannerModelViewset,basename='headbanner')
router.register('outworklist',apiviews.ourworkModelViewset,basename='outworklist')