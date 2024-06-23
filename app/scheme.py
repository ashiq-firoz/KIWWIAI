'''Defines the input and output objects of APIs'''
from enum import Enum
from pydantic import BaseModel


class Success(BaseModel):
    message: str


class Error(BaseModel):
    error: str
    statusCode: int

class Mediatype(Enum):
    '''Media Types supported'''
    IMAGE = "IMAGE"

class Task(Enum):
    '''Prediction Tasks supported'''
    MUDRA = "Kathakali-Mudra-Recognition"
    WORD = "Kathakali-Word-Recognition"
    SIGN_ALPHA = "ISL-Finger-Spell-Recognition"
    SIGN_WORD = "ISL-Words-Recognition"
    GESTURE = "Gesture Tokenization"

class Approach(Enum):
    '''Approaches that can be used'''
    PIXEL_BASED = "Pixel-Based-Approach"
    PEAK_POSE = "Peak_Pose-Based-Approach"
    KATNA = "Katna-Based-Approach"
    MOVINET = "MoviNet-Based-Approach"

class BackendFrameworks(Enum):
    '''Web Dev Frameworks supported'''
    EXPRESS = "ExpressJS"
    RUST = "RUSTJS"


