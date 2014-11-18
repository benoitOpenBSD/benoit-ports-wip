# $OpenBSD

COMMENT =		Python module that implements the SSH2 protocol

MODPY_EGG_VERSION = 	1.7.14
DISTNAME = 		ssh-${MODPY_EGG_VERSION}
PKGNAME = 		py-${DISTNAME}
CATEGORIES = 		security

HOMEPAGE = 		http://pypi.python.org/pypi/ssh/

MAINTAINER = 		Benoit Lecocq <benoit@openbsd.org>

# LGPL
PERMIT_PACKAGE_CDROM = 	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=s/ssh/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		security/py-crypto
TEST_DEPENDS =		${RUN_DEPENDS}

do-test:
			cd ${WRKSRC} && ${MODPY_BIN} test.py --verbose
        
.include <bsd.port.mk>
