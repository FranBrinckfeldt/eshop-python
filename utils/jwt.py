import os, time, jwt

def generate_token(payload, exp_minutes = 1440):
    base_payload = {
        'exp' : time.time() + (60*exp_minutes), 
        'iat' : time.time()
    }
    base_payload.update(payload)
    return jwt.encode(base_payload, os.getenv('SECRET'), algorithm='HS256')

def validate_token(authorization, sub = None):
    try:
        split_auth = authorization.split(' ')
        if split_auth[0] != 'Bearer':
            raise Exception
        decoded_token = jwt.decode(split_auth[1], os.getenv('SECRET'), algorithm='HS256')
    except: 
        return False, 'INVALID_TOKEN'
    if decoded_token['exp'] < time.time():
        return False, 'TOKEN_EXPIRED'
    elif sub != None and decoded_token['sub'] != sub:
        return False, 'INVALID_SUB'
    else:
        return True, decoded_token
