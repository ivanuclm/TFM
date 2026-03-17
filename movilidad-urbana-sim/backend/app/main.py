from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_osrm import router as osrm_router
from app.api.routes_gtfs import router as gtfs_router
from app.api.routes_otp import router as otp_router
from app.api.routes_lpmc import router as lpmc_router


app = FastAPI(title="Urban Mobility Simulator API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ya afinaremos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(osrm_router, prefix="/api/osrm", tags=["osrm"])
app.include_router(gtfs_router)
app.include_router(otp_router)
app.include_router(lpmc_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
