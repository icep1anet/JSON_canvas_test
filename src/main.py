from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.canvas.root import canvas_router

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# # 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS回避のための記述
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーティングの設定
app.include_router(canvas_router, prefix="/canvas")

@app.get("/")
async def root():
    return {"message": "Hello World"}
