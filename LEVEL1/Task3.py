def email_validation(email):
    '''email must have non empty local part and domain part befor and after @ '''
    allowed_chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890._-'
    for ch in email:
        if ch not in allowed_chars:
            return False
    '''email must contain one @ symbol'''
    if email.count('@') != 1:
        return False
    local,domain=email.split('@')
    if not local or not domain :
        return False
    if '.'  not in domain:
        return False
    if '..' in email:
        return False
    if domain.startswith('.') or domain.endswith('.') or domain.startswith('_') or domain.endswith('_'):
        return False
    if local[0] in '._' or local[1] in '._' or domain[0] in '._' or domain[-1] in '._':
        return False
    return True
email=input("Enter the Email Address:")
if email_validation(email):
    print("Valid Email")
else:
    print("Invalid Email")