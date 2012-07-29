# $OpenBSD$

COMMENT =		vSphere SDK for python.

MODPY_EGG_VERSION =	0.1.6
DISTNAME =		pysphere-${MODPY_EGG_VERSION}
PKGNAME =		py-sphere-${MODPY_EGG_VERSION}
CATEGORIES =		sysutils

HOMEPAGE =		http://code.google.com/p/pysphere/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://pysphere.googlecode.com/files/
EXTRACT_SUFX =		.zip
UNZIP =			unzip -a

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

NO_REGRESS =		Yes

.include <bsd.port.mk>
