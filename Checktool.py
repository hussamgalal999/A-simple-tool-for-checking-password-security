import re

def check_password_strength(password):
     # Minimum number of characters
     min_length = 8
    
     # Contains uppercase and lowercase letters, numbers and symbols
     if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password) or not re.search(r"\d", password) or not re.search( r"\W", password):
         return "Password must contain uppercase and lowercase letters, numbers, and symbols."

     # Minimum password length
     if len(password) < min_length:
         return f"Password must be at least {min_length} characters."

     return "Password accepted. Looks strong!"

if __name__ == "__main__":
     user_password = input("Enter password:")
     result = check_password_strength(user_password)
     print(result)
