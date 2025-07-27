INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # Ensure this is included
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'accounts',
    # Add your other apps here
]
AUTH_USER_MODEL = 'accounts.CustomUser'
DEBUG = False
ALLOWED_HOSTS = ['sila.com']  # Replace with your domain or IP addresses

# Enable XSS filtering in browsers
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking by blocking rendering on other sites
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from interpreting files as something else (e.g., from HTML to JSON)
SECURE_CONTENT_TYPE_NOSNIFF = True

# Ensure cookies are sent over HTTPS only
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True  # Redirect HTTP to HTTPS
SECURE_HSTS_SECONDS = 3600  # Set HSTS for one hour (can be adjusted)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browsers to preload HSTS policy

SECURE_SSL_REDIRECT = True
# Enforce HTTPS for one year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000  # 1 year

# Apply HSTS to all subdomains as well
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow browsers to preload the HSTS policy for your domain
SECURE_HSTS_PRELOAD = True
# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True
# Prevent clickjacking by blocking your site from being framed
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser's XSS filtering to prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True