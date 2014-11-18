# $OpenBSD$

COMMENT =		python wrapper for bcrypt

MODPY_EGG_VERSION =	1.2.2
DISTNAME =		Bcryptor-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME:L}

CATEGORIES =		security

HOMEPAGE =		http://www.bitbucket.org/ares/bcryptor/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ISC
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=B/Bcryptor/}

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		lang/cython
RUN_DEPENDS =		sysutils/py-yamlog
TEST_DEPENDS =		devel/py-nose \
			${RUN_DEPENDS}

pre-build:
			cd ${WRKSRC} && /usr/local/bin/cython lib/bcryptor/wrap/engine.pyx

.include <bsd.port.mk>
