from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from src.summary.abc import ABCSummaryService
from src.summary.dependencies import get_service
from src.summary.schema import SummarytResponseModel

router = APIRouter(tags=["Summary about all product [analyze]"], prefix="/summary")


@router.get("/", response_model=SummarytResponseModel)
def get(
    service: ABCSummaryService = Depends(get_service),
    q: Optional[str] = Query(None),
):
    try:
        data = service.get_recent(name=q)
        return {"data": list(data)}

    except BaseException as error:
        print(error)
        raise HTTPException(status_code=404, detail=str(error))
