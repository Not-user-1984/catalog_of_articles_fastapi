from fastapi import FastAPI

from config import settings

from customer.router import router as customer_router


app = FastAPI(
    title=settings.app_title,
    description=settings.description,
)


app.include_router(trade_router, tags=["Trade crud"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
