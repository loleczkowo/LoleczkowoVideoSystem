from .login import router as login_router
from .signup import router as signup_router
from .reports import router as reports_router

all_routers = [login_router, signup_router, reports_router]
