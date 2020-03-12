# $OpenBSD$

COMMENT =	reading information and extracting from UBI-UBIFS images

MODPY_EGG_VERSION =	0.6.3
DISTNAME =	ubi_reader-${MODPY_EGG_VERSION}
PKGNAME =	py-${DISTNAME}

CATEGORIES =	sysutils

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

HOMEPAGE =	https://github.com/jrspruitt/ubi_reader

# GPLv3
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =    jrspruitt
GH_PROJECT =    ubi_reader
GH_COMMIT =	5579cb8acf63c62e7c7be8ab342ddf555cd3b001

MODULES =	lang/python
MODPY_SETUPTOOLS = Yes

FLAVORS =	python3
FLAVOR ?=	python3

RUN_DEPENDS =	archivers/py-lzo2

pre-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/py-ubi_reader
		${INSTALL_DATA} ${WRKSRC}/README.md ${PREFIX}/share/doc/py-ubi_reader
 
NO_TEST =	Yes

.include <bsd.port.mk>
