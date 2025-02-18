from typing import Any
from fastapi import Depends
from auth.dependencies import AUTHENTICATION_MODE, authenticate_analytics, authenticate_workbench


def load_auth_mode() -> list[Any] | None:
    match AUTHENTICATION_MODE:
        case "noauth":
            return None
        case "workbench":
            AUTH_DEPENDENCY = [Depends(authenticate_workbench)]
        case "analytics":
            AUTH_DEPENDENCY = [Depends(authenticate_analytics)]
        case _:
            raise ValueError(f"Unknown authentication mode: {AUTHENTICATION_MODE}")
    return AUTH_DEPENDENCY
