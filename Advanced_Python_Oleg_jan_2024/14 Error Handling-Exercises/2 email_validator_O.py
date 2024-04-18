class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

EMAIL_MIN_LENGHT = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(email.split('@')[0]) <= EMAIL_MIN_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = '.' + email.split(".")[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    Ne e vqrna