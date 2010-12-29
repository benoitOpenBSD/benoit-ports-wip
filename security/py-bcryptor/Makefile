# $OpenBSD$

COMMENT =		python wrapper for bcrypt

MODPY_EGG_VERSION =	1.1
DISTNAME =		bcryptor-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}

CATEGORIES =		security

HOMEPAGE =		http://www.bitbucket.org/ares/bcryptor/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache License, v2.0
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=b/bcryptor/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		devel/pyrex

REGRESS_DEPENDS =	devel/py-nose

.include <bsd.port.mk>
