# This .py is used for authenticating user and 
# authenticating token, comparing hashed passwords  
# general credential validation
# cryptography and authorization section
import secrets
from argon2 import PasswordHasher
from argon2.exceptions import HashingError


def authenticate():
    pass
    
def hash_pwd(pwd: str) -> str:
    """Simple function for one-way hashing
    Args: 
        password: str
        passes unhashed password
    Returns:
        salted and hashed password
    
    
    """
    try:
        ph = PasswordHasher()
        hashed_pwd = ph.hash(password=pwd)

        return hashed_pwd
    except HashingError as he:
        print(f'ERROR: {he}')

        raise ValueError('Error hashing password') from he

def verify_pwd(pwd: str, hashed_pwd:str) -> bool:
    """Simple function that verifies a password
    Args:
        pwd: str
        Passes passwdord in raw format

        hashed_pwd: str
        Passes hashed password
    Returns:
        returns bool
    """
    ph = PasswordHasher()

    return ph.verify(password=pwd, hash=hashed_pwd)

def create_token():
    pass

# def confirm_password():
#     user_cred = (user_login.username, user_login.email)
#     find_user = get_user(db=db, user_cred=user_cred)
#     if find_user:
        
        
    

#         # this section goes to security directory
#         # salt = secrets.token_bytes(16)

#         db_hash_salt = find_user.hashed_password.split(':')
#         input_salted_pass = db_hash_salt[0] + user_login.password 

#         ph = PasswordHasher()

#         hashed_input_p = ph.hash(input_salted_pass)

        

#         if ph.verify(db_hash_salt[1], hashed_input_p):
            
#             # 1. convert to json
#             # 2. put find_user to json
#             # 3. generate token
#             # 4. put token to json
#             # 5. return the variable
#             pass
#             # and then we return a user template in json/xml or whatever form
#             # we also generate token for cookie/session adn then return that also
#             # we return user info

password = '123Password'
wrong_password = '122Password'
result = hash_pwd(pwd=password)

print('verifying correct pwds')
print(verify_pwd(password, result))


