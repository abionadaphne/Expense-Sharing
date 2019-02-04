########################### Notice To Github Viewers #############################
# This is a mocked file intended to represent 'config.py' in the actual project. #
# Because 'config.py' contains database credentials, it has been omitted.        #
##################################################################################

import os
basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True

SECRET_KEY = "S0M3S3CR3TK3V" # Necessary for Flask session.           Example: "S0M3S3CR3TK3Y"

HOST       = "127.0.0.1" # OpenShift Database IP.                 Example: "127.99.99.9"
LOCALHOST  = "127.0.0.1" # Local Database IP for Port Forwarding. Example: "127.0.0.1"
USERNAME   = "abiona_daphne" # Database username.                     Example: "admin-user"
PASSWORD   = "Daphne@23071998" # Database password.                     Example: "secret-pw"
DB_NAME    = "expense_sharing" # Database name.                         Example: "expensetracker"