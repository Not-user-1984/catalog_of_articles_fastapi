from fastapi import HTTPException


async def check_authorization(user):
    if not user:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return user


def check_admin(user):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="You are not an admin")
    return user
