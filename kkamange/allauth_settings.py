
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_FORMS={'signup':'user.forms.CustomSignupForm'}
# 이메일 인증 여부
ACCOUNT_EMAIL_VERIFICATION = 'none'

