# $OpenBSD$

COMMENT =		MD6 wrapper for Python

MODPY_EGG_VERSION =	0.1a2
DISTNAME =		md6-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		security

HOMEPAGE =		http://pypi.python.org/pypi/md6/0.1a2

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		ssl crypto

MASTER_SITES =		${MASTER_SITE_PYPI:=m/md6/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

.include <bsd.port.mk>
