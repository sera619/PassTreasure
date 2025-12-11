import string
import random


class PasswordGenerator:
    def __init__(self, 
                 length: int = 12,
                 use_upper: bool = True,
                 use_numbers: bool = True,
                 use_special: bool = True,
                 excluded_chars: list[str] = []):
        self.length = length
        self.use_upper = use_upper
        self.use_numbers = use_numbers
        self.use_special = use_special
        self.excluded_chars = excluded_chars
    
    def generate(self) -> str:
        if self.length <= 0:
            raise ValueError("Password length must be greater than 0.")        
                 
        default_special_char_set = "!#$%()*+,-./:;=?@[]^_{|}~"
        char_set = string.ascii_lowercase
        if self.use_upper:
            char_set += string.ascii_uppercase
        if self.use_numbers:
            char_set += string.digits
        if self.use_special:
            special_char_set = ""
            
            for char in default_special_char_set:
                if char in self.excluded_chars:
                    continue
                special_char_set += char
            char_set += special_char_set

        if not char_set:
            raise ValueError("No characters available to generate password")

        # Ensure at least one character from each selected category
        password_chars = []
        password_chars.append(random.choice(string.ascii_lowercase))
        if self.use_upper:
            password_chars.append(random.choice(string.ascii_uppercase))
        if self.use_numbers:
            password_chars.append(random.choice(string.digits))
        if self.use_special:
            password_chars.append(random.choice(special_char_set))

        # Fill the rest of the password
        while len(password_chars) < self.length:
            password_chars.append(random.choice(char_set))

        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)

        return ''.join(password_chars)