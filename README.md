# Password-Vault-System
This project is to show list of password and other related data for authenticated users.
----------------------------------------------------------------------------------------
# Installation Process


# Note
- Under settings.py file:
  EMAIL_HOST_USER = '' - add your email
  EMAIL_HOST_PASSWORD = '' -add your password
  DEFAULT_FROM_EMAIL = 'Celery <>' - inside <> add your email

# Features
1. Users can signup and login (include both email/password and google login).
3. Users once logged in can view their list of stored password
4. Users can save new password (password must be encrypted while saving and decrypted while retrieving, assume relent fields while creating form for password storage)
5. Send periodic notification to user's email to change old password (assume suitable period) 
