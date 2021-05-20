from pydantic import BaseModel
from enum import Enum
from typing import List


class Resolution(BaseModel):
    width: int
    height: int


class SessionAction(BaseModel):
    ip: str
    resolution: Resolution


class SessionLocationDetails(BaseModel):
    country: str
    country_code: str
    region: str
    city: str
    latitude: float
    longitude: float


class SessionActionType(str, Enum):
    login = "login"
    logout = "logout"
    buy = "buy"
    review = "review"
    shopping_cart = "shopping-cart"


class ResponseModel(BaseModel):
    action: SessionActionType
    info: SessionAction
    location: SessionLocationDetails
    action_date: str


class FailedResponseModel(BaseModel):
    errors: List[dict]
