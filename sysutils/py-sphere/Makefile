
COMMENT =		vSphere SDK for python.

MODPY_EGG_VERSION =	0.1.8
DISTNAME =		pysphere-${MODPY_EGG_VERSION}
PKGNAME =		py-sphere-${MODPY_EGG_VERSION}
CATEGORIES =		sysutils

HOMEPAGE =		http://code.google.com/p/pysphere/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

SITES =			http://pysphere.googlecode.com/files/
EXTRACT_SUFX =		.zip
UNZIP =			unzip -a

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

NO_TEST =		Yes

post-install:
			find ${WRKINST}${MODPY_SITEPKG} -type f -exec chmod 444 {} \;

.include <bsd.port.mk>
