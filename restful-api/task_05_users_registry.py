"""Module holding a users's registry for use in task 5"""
from werkzeug.security import generate_password_hash  # Required for encryption

# NOTE: generate_password_hash adds a random element (salt)
#   each time it's called so normally for the same string provided n times
#   we'd get n unique hashes.
# It's a different design than JWT which are "close to unique" because
#   constituted from variable parts: "identity" (structure defined by dev),
#   and "temporal claims" injected by extension:
#   (iat=issued at, exp=expiration date, jti=random uuid)
users = {
    # --- User role: nominal case ---
    "user_standard": {
        "username": "user_standard",
        "password": generate_password_hash("password123"),
        "role": "user"
    },
    # Variant: password with special characters
    "user_special_pwd": {
        "username": "user_special_pwd",
        "password": generate_password_hash("P@$$w0rd!"),
        "role": "user"
    },
    # Variant: username with mixed case to ensure case-sensitive lookup
    "User_CaseSensitive": {
        "username": "User_CaseSensitive",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    # Variant: username with digits
    "user_007": {
        "username": "user_007",
        "password": generate_password_hash("bondpass"),
        "role": "user"
    },

    # --- Admin role: nominal case ---
    "admin_main": {
        "username": "admin_main",
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    # Variant: additional admin to check control relies on role not username.
    "admin_secondary": {
        "username": "admin_secondary",
        "password": generate_password_hash("adminpass2"),
        "role": "admin"
    },

    # --- Writer role (personal addition): nominal case ---
    "writer_alice": {
        "username": "writer_alice",
        "password": generate_password_hash("alicepass"),
        "role": "writer"
    },
    "writer_bob": {
        "username": "writer_bob",
        "password": generate_password_hash("bobpass"),
        "role": "writer"
    },

    # --- EDGE CASES ---
    # Overly long username → stressing size limit/robustness of token/lookup
    "user_with_a_very_long_username_that_pushes_limits": {
        "username": "user_with_a_very_long_username_that_pushes_limits",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    # Same pwd as user_standard → ensuring each hash is unique
    "user_same_pwd_as_standard": {
        "username": "user_same_pwd_as_standard",
        "password": generate_password_hash("password123"),
        "role": "user"
    },
}
