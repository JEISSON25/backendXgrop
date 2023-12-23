from rest_framework.routers import DefaultRouter
from ..account.views import *
from ..products.views import *
from ..sales.views import *

router = DefaultRouter()

router.register(r'accounts', AccountViewset, basename='accounts')
router.register(r'typeaccounts', TypeAccountViewset, basename='typeaccounts')
router.register(r'products', ProductsViewset, basename='products')
router.register(r'sales', SalesViewset, basename='sales')
# router.register(r'detailsales', DetailSalesViewset, basename='detailsales')
router.register(r'register', AccountCreateView, basename='user')
router.register(r'salesProducts', SalesProductViewset,
                basename='salesproducts')

urlpatterns = router.urls
