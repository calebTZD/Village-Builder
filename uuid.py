import uuid
from enum import Enum

def generateID():
    return str(uuid.uuid4()).replace('-','')