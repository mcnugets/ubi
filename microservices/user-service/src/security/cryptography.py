# We use this .py for handling:
# hashing function logic, JWS token generation/session, encrtyption an decryption
# how we perform hashing?
# first generate salt, then concatenate with generated salt, hash it, concatenate with non hashed generated salt
# use delimiter: salt + : + hashed password, then store in db