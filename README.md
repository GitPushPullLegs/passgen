# Passgen
A small library to quickly generate random passwords.

⚠️ **Extremely simple, not recommended for use. We're only using this in a very limited capacity.**

## Installation :
`pip install git+https://github.com/GitPushPullLegs/passgen.git`

## Quickstart:

```python
import passgen

password = passgen.generate_mnemonic_password(word_count=5)
password2 = passgen.generate_alphanumeric_password(character_count=10)

# That's it, there's nothing else, nothing fancy.
```