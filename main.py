import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from core.middleware import ProcessTimeMiddleware
from services.auth.routers.auth import auth_router
from services.auth.routers.user import user_router

app = FastAPI(title="Topskill API",
              docs_url="/docs",
              openapi_url="/docs/api")

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*", "topskill.uz"]
)
app.add_middleware(ProcessTimeMiddleware)

origins = [
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(user_router, prefix='/users', tags=['User'])


# @app.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.message}
#     )


# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except BaseException as e:
#         print(e)
#         # you probably want some kind of logging here
#         return JSONResponse({"detail": "Internal server error"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# app.middleware('http')(catch_exceptions_middleware)

if __name__ == '__main__':
    uvicorn.run("__main__:app", host='0.0.0.0', port=8080, reload=True, workers=1)
