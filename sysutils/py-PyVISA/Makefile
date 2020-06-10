# $OpenBSD$

COMMENT =		python VISA bindings for GPIB, RS232, USB instruments

MODPY_EGG_VERSION =	0.4.1
DISTNAME =		PyVISA-py-${MODPY_EGG_VERSION}
PKGNAME =		py-PyVISA-${MODPY_EGG_VERSION}
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

HOMEPAGE =		https://github.com/pyvisa/pyvisa-py

# MIT
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

RUN_DEPENDS =		devel/py-serial${MODPY_FLAVOR} \
			devel/pyusb${MODPY_FLAVOR} \
			sysutils/py-VISA${MODPY_FLAVOR}

.include <bsd.port.mk>
