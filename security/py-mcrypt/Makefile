# $OpenBSD$

COMMENT =		Python interface to mcrypt library

MODPY_EGG_VERSION =	1.1
DISTNAME =		python-mcrypt-${MODPY_EGG_VERSION}
PKGNAME =		py-mcrypt-${MODPY_EGG_VERSION}
CATEGORIES =		security

HOMEPAGE =		http://labix.org/python-mcrypt

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv2.1
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://labix.org/download/python-mcrypt/

MODULES =		lang/python
#MODPY_SETUPTOOLS =	Yes

LIB_DEPENDS =		security/libmcrypt

pre-configure:
		${SUBST_CMD} ${WRKSRC}/setup.py

do-regress: fake
		@cd ${WRKSRC} && ${MAKE_ENV} \
		PYTHONPATH=${WRKINST}${MODPY_SITEPKG} ${MODPY_BIN} ./test.py 

.include <bsd.port.mk>
