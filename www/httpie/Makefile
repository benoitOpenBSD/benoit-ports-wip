# $OpenBSD$

COMMENT =		HTTPie is a CLI, cURL-like tool for humans

MODPY_EGG_VERSION =	0.6.0
DISTNAME =		httpie-${MODPY_EGG_VERSION}
CATEGORIES =		www

HOMEPAGE =		https://github.com/jkbr/httpie

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=h/httpie/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		textproc/py-pygments \
			www/py-requests
BUILD_DEPENDS =		${RUN_DEPENDS}

NO_TEST =		Yes

.include <bsd.port.mk>
