from fastapi.security import OAuth2PasswordBearer

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/auth/jwt/login",
    scheme_name="JWT",
    description="Topskill API JWT Auth"
)
