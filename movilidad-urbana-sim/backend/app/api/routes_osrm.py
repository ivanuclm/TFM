from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.osrm_client import Profile, get_route

router = APIRouter()


class Point(BaseModel):
    lat: float = Field(..., description="Latitude")
    lon: float = Field(..., description="Longitude")


class RouteRequest(BaseModel):
    origin: Point
    destination: Point
    profiles: List[Profile] = ["driving", "cycling", "foot"]


class RouteResult(BaseModel):
    profile: Profile
    distance_m: float
    duration_s: float
    geometry: List[Point]


class RouteResponse(BaseModel):
    origin: Point
    destination: Point
    results: List[RouteResult]


@router.post("/routes", response_model=RouteResponse)
async def get_routes(body: RouteRequest):
    results: List[RouteResult] = []
    for profile in body.profiles:
        route = await get_route(
            profile,
            body.origin.lon,
            body.origin.lat,
            body.destination.lon,
            body.destination.lat,
        )
        results.append(RouteResult(**route))
    return RouteResponse(origin=body.origin, destination=body.destination, results=results)
