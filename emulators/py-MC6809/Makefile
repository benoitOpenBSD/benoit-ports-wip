# $OpenBSD$

COMMENT =		implementation of the MC6809 CPU in Python

MODPY_EGG_VERSION = 	0.6.0
DISTNAME =		MC6809-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		emulators

HOMEPAGE =		https://github.com/6809/MC6809

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes

FLAVORS =		python3
FLAVOR ?=		python3

# Searching for click<8.0,>=7.0
RUN_DEPENDS =		devel/py-click${MODPY_FLAVOR}

.include <bsd.port.mk>
