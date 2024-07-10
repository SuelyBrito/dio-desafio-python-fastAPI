from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
#if __name__ == "__main__":
#    uvicorn.run(app, host="127.0.0.1", port=5049)