# $OpenBSD$

COMMENT =		python implementation of DES and TRIPLE DES algorithm

MODPY_EGG_VERSION =	2.0.1
DISTNAME =		pyDes-${MODPY_EGG_VERSION}
PKGNAME =		py-des-${MODPY_EGG_VERSION}

CATEGORIES =		security

HOMEPAGE =		http://twhiteman.netfirms.com/des.html

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Public Domain
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://twhiteman.netfirms.com/pyDES/

MODULES =		lang/python

do-regress: fake
			@cd ${WRKSRC} && ${MAKE_ENV} \
			PYTHONPATH=${WRKINST}${MODPY_SITEPKG} ${MODPY_BIN} ./test_pydes.py

.include <bsd.port.mk>
