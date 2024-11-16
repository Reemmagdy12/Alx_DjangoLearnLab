This is my django project
In this project I added some permissions on the Book model like can_create,can _edit and can_delete 
And then I added these permissions on some of the views after assigning them to the grpups :
Viewers have only can_view permission
Editors have can_view, can_create and can_edit permissions 
Admins have can_view, can_create, can_edit and can_delete permissions 

In this project I did some security settings in settings.py :
SECURE_SSL_REDIRECT: Set to True to redirect all non-HTTPS requests to HTTPS.
SECURE_HSTS_SECONDS: Set an appropriate value (e.g., 31536000 for one year) to instruct browsers to only access the site via HTTPS for the specified time.
SECURE_HSTS_INCLUDE_SUBDOMAINS and SECURE_HSTS_PRELOAD: Set to True to include all subdomains in the HSTS policy and to allow preloading.
SESSION_COOKIE_SECURE: Set to True to ensure session cookies are only transmitted over HTTPS.
CSRF_COOKIE_SECURE: Set to True to ensure CSRF cookies are only transmitted over HTTPS.
X_FRAME_OPTIONS: Set to “DENY” to prevent your site from being framed and protect against clickjacking.
SECURE_CONTENT_TYPE_NOSNIFF: Set to True to prevent browsers from MIME-sniffing a response away from the declared content-type.
SECURE_BROWSER_XSS_FILTER: Set to True to enable the browser’s XSS filtering and help prevent cross-site scripting attacks.
Ensure that your deployment environment is configured to support HTTPS by setting up SSL/TLS certificates. 