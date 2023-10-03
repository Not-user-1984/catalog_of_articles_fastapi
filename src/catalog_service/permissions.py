# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from db.database import get_async_session

# # Зависимость для проверки, что пользователь аутентифицирован
# def get_current_user(db: Session = Depends(get_async_session)):
#     # Ваш код аутентификации, например, с использованием JWT или сессий
#     # Верните объект пользователя, если аутентификация успешна
#     # Или выбросьте исключение HTTPException с кодом 401 (Unauthorized)
#     user = authenticate_user(db)
#     if not user:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return user

# # Зависимость для проверки, что пользователь имеет разрешение на выполнение действия
# def has_permission(user: models.User = Depends(get_current_user)):
#     # Ваш код проверки разрешений для пользователя
#     # Верните True, если пользователь имеет разрешение, иначе False
#     if user.has_permission_to_do_something():
#         return True
#     return False