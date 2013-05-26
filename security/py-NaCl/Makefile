# $OpenBSD

COMMENT =		Python binding to the NaCl library

MODPY_EGG_VERSION = 	0.1.0
DISTNAME = 		PyNaCl-${MODPY_EGG_VERSION}
PKGNAME = 		py-NaCl-${DISTNAME}
CATEGORIES = 		security

HOMEPAGE = 		https://github.com/dstufft/pynacl

MAINTAINER = 		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM = 	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=P/PyNaCl/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		security/libsodium
BUILD_DEPENDS =		${RUN_DEPENDS}
TEST_DEPENDS =		devel/py-test \
			devel/py-cffi

.include <bsd.port.mk>
