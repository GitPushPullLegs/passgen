import random
import string
from .words import WORDS

__version__ = '0.0.1'
__author__ = 'Joe Aguilar'

def generate_mnemonic_password(word_count: int = 4):
    """Generates a mnemonic password."""
    return '-'.join([random.choice(WORDS) for _ in range(0, word_count)])


def generate_alphanumeric_password(character_count: int = 8):
    """Generates an alphanumeric password."""
    chars = string.ascii_letters + string.digits
    password = ''.join([random.choice(chars) for _ in range(0, character_count)])
    random_characters_count = random.randint(0, int(character_count / 3))
    while random_characters_count >= 0:
        random_symbol = random.randint(0, character_count)
        password = password[:random_symbol] + random.choice(r"~!@#$%^&*()_-+={[}]\:;?/") + password[random_symbol:]
        random_characters_count -= 1
    return password
