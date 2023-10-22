
COMMENT =		Python bindings for the LZO data compression library 

MODPY_EGG_VERSION = 	1.12
DISTNAME =		python-lzo-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME:S/python-lzo/lzo2/}
CATEGORIES =		archivers

HOMEPAGE =		https://github.com/jd-boyd/python-lzo

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MODULES =		lang/python
MODPY_PI =		Yes

FLAVORS =		python3
FLAVOR =		python3

WANTLIB +=		pthread ${MODPY_WANTLIB}

BUILD_DEPENDS =		archivers/lzo2

NO_TEST =		Yes

.include <bsd.port.mk>
