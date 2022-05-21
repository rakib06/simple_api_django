# S3 BUCKETS CONFIG
'''
# AWS_ACCESS_KEY_ID = 'AKIAQ7KLZJXGOENX2XTT'
# AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rkx-test'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_FILE_OVERWRITE = False

'''
'''
<?xml version = "1.0" encoding = "UTF-8"?>
<CORSConfiguration xmlns = "http://s3.amazonaws.com/doc/2006-03-01/" >
<CORSRule >
    <AllowedOrigin > * < /AllowedOrigin >
    <AllowedMethod > GET < /AllowedMethod >
    <AllowedMethod > POST < /AllowedMethod >
    <AllowedMethod > PUT < /AllowedMethod >
    <AllowedHeader > * < /AllowedHeader >
</CORSRule >
</CORSConfiguration >
'''
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['http://localhost:3000', '127.0.0.1']
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
]

AWS_ACCESS_KEY_ID = 'AKIAQ7KLZJXGHOYLWLWI'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'rk-s3-bucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_LOCATION = 'static_files'

'''
# Ignore aws for static file access

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = 'https://rk-s3-bucket.s3.ap-south-1.amazonaws.com/'


'''

# STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATIC_URL = 'https://rk-s3-bucket.s3.amazonaws.com/'

DEFAULT_FILE_STORAGE = 'home.settings.storage_backends.MediaStorage'
AWS_DEFAULT_ACL = None
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
'''
