from rest_framework.routers import DefaultRouter
from . import views as apiviews
#creating router object
router = DefaultRouter()
router.register('ourworkcat',apiviews.ourWork_catModelViewset,basename='ourwork')
router.register('ourcatbanner',apiviews.headbannerModelViewset,basename='headbanner')
router.register('outworklist',apiviews.ourworkModelViewset,basename='outworklist')
router.register('ourservicecat',apiviews.ourServiceModelViewset,basename='ourservicecat')
router.register('servicebanner',apiviews.ServiceHeadbannerModelViewset,basename='servicebanner')
router.register('subservice',apiviews.subServiceModelViewset,basename='subservice')
router.register('servicesubmenu',apiviews.serviceSubMenuModelViewset,basename='servicesubmenu')