from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime

from schemas.schema import SessionAction
from schemas.schema import SessionActionType
from schemas.schema import ResponseModel
from schemas.schema import FailedResponseModel
from api import utils


app = FastAPI()


@app.post(
    "/track/{action}",
    response_model=ResponseModel,
    responses={400: {"model": FailedResponseModel}}
)
async def track_action(action: SessionActionType, body: SessionAction):
    location, errors = utils.get_ip_info(body.ip)

    if len(errors) > 0:
        return JSONResponse(
            status_code=400,
            content={"errors": errors})

    return {
        "action": action,
        "info": body,
        "location": location,
        "action_date": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }
