django-oidc-auth
================

An OpenID Connect Client for Django.


HOW TO USE
----------

First things first, so:

    $ pip install django-oidc-auth

This release targets Django >= 5.2,<5.3 and Python 3.12.

Then add this to your settings:

    INSTALLED_APPS = (
        # ...
        'oidc_auth',
        # ...
    )

    # Put all custom configurations inside this dict
    OIDC_AUTH = {
        'SCOPES': ('openid', 'preferred_username', 'email', 'profile'),
    }

    LOGIN_URL = 'oidc-login'
    LOGIN_REDIRECT_URL = '/'

    AUTHENTICATION_BACKENDS = (
        'oidc_auth.auth.OpenIDConnectBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

Set the following environment variables before running the project:

    export DJANGO_SECRET_KEY='replace-this-with-a-long-random-string'
    export DJANGO_DEBUG=on  # optional for local development
    export DJANGO_SECURE_SSL_REDIRECT=off  # optional if you cannot use HTTPS locally

Finally, add this to your *urls.py*:

    from django.urls import include, path
    from your import views

    urlpatterns = [
        # ...
        path('', views.index, name='index'),
        path('oidc/', include('oidc_auth.urls')),
    ]

Run `python manage.py migrate` and you're ready (*kinda*).

VALIDATION
----------

After installing the new dependencies, run:

    python manage.py check --deploy
    pytest
    tox -e py312

The checks ensure Django 5.2 compatibility, the pytest suite verifies the
OIDC login/complete flow, and the tox environment mirrors the CI matrix.

<!--
#TODO
#----
#
#Primeiro, faz o discovery e obtem todos os dados do sistema.
#
#Grava os endpoints.
#
#Segundo, faz o register e então inicia o trabalho de autenticação
-->

<!-- Consumer Action Items

Upgrade Django: Ensure your app now runs on Django 5.2.x (and Python 3.12) before upgrading to the latest django-oidc-auth. Update your own requirements.txt/pyproject accordingly and rerun your test suite under Django 5.2.

Install matching dependency version: Pin the new django-oidc-auth release (pip install django-oidc-auth>=… once published) so you pick up the Django 5-compatible code.

Update URL config samples: If your project still uses legacy urlpatterns = patterns(...) style (as shown in the old README), switch to path()/include() like in the updated documentation to avoid deprecation issues in Django 5.

Set security env vars: Provide environment overrides for the new defaults exposed in settings.py:5-70—at minimum DJANGO_SECRET_KEY, and, when running locally without HTTPS, set DJANGO_SECURE_SSL_REDIRECT=off. These are read only when you run this sample project, but the README now documents them and they’re useful patterns for your own deployment configuration.

Re-run validations: After upgrading, execute python [manage.py](http://_vscodecontentref_/8) check --deploy, your pytest suite, and any tox environments you rely on to confirm your consumer project remains green under Django 5.2 and the new OIDC client.

No other API changes were introduced, so your integration points (AUTHENTICATION_BACKENDS, URLs, templates) remain the same. -->
