from .login import router as login_router
from .signup import router as signup_router
# from .reports import router as reports_router
from .test_connection import router as test_connection_router
from .logout import router as logout_router

all_routers = [login_router,
               signup_router,
               logout_router,
               # reports_router,
               test_connection_router]
