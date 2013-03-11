# $OpenBSD$

COMMENT =		logging in YAML format

MODPY_EGG_VERSION =	0.9
DISTNAME =		Yamlog-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME:L}

CATEGORIES =		sysutils

HOMEPAGE =		http://www.bitbucket.org/ares/bcryptor/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ISC
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=Y/Yamlog/}

MODULES =		lang/python

MODPY_SETUPTOOLS =	Yes

TEST_DEPENDS =		devel/py-nose \
			devel/py-coverage

.include <bsd.port.mk>
