# This .py is used for authenticating user and 
# authenticating token, comparing hashed passwords  
# general credential validation
# cryptography and authorization section
import secrets
import jwt
import dotenv 
import os
from datetime import datetime, timedelta, timezone
from typing import Union, Annotated, Dict, Optional
from argon2 import PasswordHasher
from argon2.exceptions import HashingError, InvalidHashError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


def authenticate(hashed_pwd: str, pwd: str) -> bool: # maybe change it later just testing
 
    
    if not verify_pwd(pwd=pwd, hashed_pwd=hashed_pwd):
        return False
        
    
    return True
    
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

def verify_pwd(pwd: str, hashed_pwd: str) -> bool:
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
    try:
        return ph.verify(password=pwd, hash=hashed_pwd)
    except InvalidHashError as inv:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Error: {inv}') from inv

def payload(data: Optional[Dict[str, str]], expiry: Union[timedelta, None] = None, iat: Union[datetime, None] = None):

    payload = data.copy()
    payload.update({'exp': expiry})
    payload.update({'iat': iat})
    return payload

def create_token(dict:  Optional[Dict[str, str]], algorithm: str,  expiry: Union[timedelta, None] = None):
    try:
        gen_str = secrets.token_bytes(16)
        ph = PasswordHasher()
        secret_key = ph.hash(gen_str)
        
        if expiry:
            exp_time  = datetime.now() + expiry
        else:
            exp_time = datetime.now() + timedelta(minutes=90)

        dict.update({'exp' : exp_time})
        
        jwt_encode = jwt.encode(payload=dict, key=secret_key, algorithm=algorithm)
        
        env_file = dotenv.find_dotenv()
        # dotenv.set_key(env_file, key_to_set='ALGORITHM', value_to_set=algorithm)
        dotenv.set_key(env_file, key_to_set='SECRET_KEY', value_to_set=secret_key)

        return jwt_encode
    except Exception as e:
            print(f'Error: {e}')
            
            
        # genereic payload template:
    # sub: username
    # id: user id
    # iat: when token created
    # exp: when token expires
    # 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]):
    auth_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="Failed to validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    
    try:
        env_file = dotenv.find_dotenv()
        dotenv.load_dotenv(env_file)

        payload = jwt.decode(jwt = token, key = os.environ['SECRET_KEY'], algorithms=os.environ['ALGORITHM'])
        
        return payload
    except auth_exception as e:
        raise e



# env_file = dotenv.find_dotenv()
# dotenv.load_dotenv(env_file)
# sc = os.environ['SECRET_KEY'] = 'IMAGINE A SECRET KEY'

# dotenv.set_key(env_file, key_to_set='SECRET_KEY', value_to_set=sc)
# print(sc)

# jwt_result = create_token({'username': 'scar', 'id' : '1'}, datetime.now() + timedelta(days=1))
# print('encoded jwt:')
# print(jwt_result)

# env_file = dotenv.find_dotenv()
# dotenv.load_dotenv(env_file)
# print('decoded jwt: ')
# print(jwt.decode(jwt=jwt_result,key=os.environ['SECRET_KEY'] ,algorithms=['HS256']))
















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

