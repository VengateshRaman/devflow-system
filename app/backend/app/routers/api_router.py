## Below is the manual import format of the routers
# from fastapi import APIRouter

# from app.routers.v1.router import router as v1_router

# api_router = APIRouter()

# api_router.include_router(
#     v1_router,
#     prefix="/v1"
# )

## Below is the automatic router finding method 
## Also in this we dont need the router.py file inside the v1

import pkgutil
import importlib
from fastapi import APIRouter

api_router = APIRouter()

package_name = "app.routers.v1"

package = importlib.import_module(package_name)

for _, module_name, _ in pkgutil.iter_modules(package.__path__):

    module = importlib.import_module(f"{package_name}.{module_name}")

    if hasattr(module, "router"):
        api_router.include_router(
            module.router,
            prefix="/v1"
        )

