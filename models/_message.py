from dataclasses import dataclass

from pydantic import BaseModel
import datetime


@dataclass
class User:
    email: str
    name: str
    username: str


@dataclass
class Message(BaseModel):
    message: str
    reviewer: User
    timestamp: datetime.datetime
