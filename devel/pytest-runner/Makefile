# $OpenBSD$

COMMENT =		scripts can use pytest-runner to add setup.py test support 

MODPY_EGG_VERSION = 	1.2
DISTNAME =		pytest-runner-${MODPY_EGG_VERSION}
CATEGORIES =		devel

HOMEPAGE =		https://bitbucket.org/jaraco/pytest-runner

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=p/pytest-runner/}
EXTRACT_SUFX =		.zip

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		devel/py-hgtools

NO_TEST =		Yes

pre-install:
			chmod 644 ${WRKSRC}/pytest_runner.egg-info/*
                        
.include <bsd.port.mk>
