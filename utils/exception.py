from fastapi import HTTPException


def build_exception(message, status_code: int) -> HTTPException:
    return HTTPException(
        status_code=status_code,
        detail=message
    )
