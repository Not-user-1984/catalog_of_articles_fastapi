from fastapi import FastAPI
from sqladmin import Admin

from admin import models_view
from auth.routers import router as auth_router
from catalog_service.routers import router as catalog_service_router
from config import settings
from db.database import engine

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
)


app.include_router(catalog_service_router, tags=["catalog_service crud"])
app.include_router(auth_router)

admin = Admin(app, engine)

admin.add_view(models_view.ArticleAdmin)
admin.add_view(models_view.ArticleCategoryAdmin)
admin.add_view(models_view.UserAdmin)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
