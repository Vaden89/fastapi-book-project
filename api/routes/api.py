from fastapi.responses import JSONResponse
from fastapi import APIRouter, status

router = APIRouter()

@router.get(
        "/test"
)
def test():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "testing"}
    )