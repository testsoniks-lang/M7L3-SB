import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_haveabcd():
    """Тест что есть буквы"""
    # Добавляем генерацию пароля внутрь этого теста:
    password = generate_password(100) 
    
    has_letters = any(char.isalpha() for char in password)
    assert has_letters is True, f"Пароль '{password}' не содержит букв"

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""