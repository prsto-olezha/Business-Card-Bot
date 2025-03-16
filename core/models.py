from beanie import Document
from pydantic import BaseModel, Field, field_validator
from phonenumbers import parse, is_valid_number, format_number, PhoneNumberFormat, phonenumberutil
import datetime as dt

class Applicant_model(Document):
    id: int
    user_name: str
    email: str
    first_name: str
    last_name: str
    number_phone: str
    status: int

    @field_validator("number_phone")
    def validate_phone_number(cls, v: str) -> str:
        """
        Валидация номера телефона с использованием библиотеки phonenumbers.
        """
        try:
            # Парсим номер телефона
            parsed_number = parse(v, None)
            
            # Проверяем, является ли номер валидным
            if not is_valid_number(parsed_number):
                raise ValueError("Номер телефона невалиден")
            
            # Возвращаем номер в международном формате
            return format_number(parsed_number, PhoneNumberFormat.E164)
        except phonenumberutil.NumberParseException as e:
            raise ValueError(f"Некорректный формат номера телефона: {e}")

    class Settings:
        name = "Applicants"
        
class User_model(Document):
    id: int
    user_name: str
    first_name: str | None = None
    last_name: str | None = None
    class Settings:
        name = "Users"