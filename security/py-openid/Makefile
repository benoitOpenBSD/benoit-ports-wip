# $OpenBSD$

COMMENT =		The OpenID library with batteries included.

MODPY_EGG_VERSION =	2.2.4
DISTNAME =		python-openid-${MODPY_EGG_VERSION}
PKGNAME =		py-openid-${MODPY_EGG_VERSION}

CATEGORIES =		security

HOMEPAGE =		http://www.openidenabled.com/python-openid/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache v2.0
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://openidenabled.com/files/python-openid/packages/

MODULES =		lang/python

DOCSDIR =               ${PREFIX}/share/doc/py-openid
DEMOSDIR =              ${PREFIX}/share/examples/py-openid

post-install:
			${INSTALL_DATA_DIR} ${DOCSDIR}
			${INSTALL_DATA} ${WRKSRC}/doc/* ${DOCSDIR}
			${INSTALL_DATA_DIR} ${DEMOSDIR}
			${INSTALL_DATA} ${WRKSRC}/examples/{*.py,README} ${DEMOSDIR}
                                                                                                
.include <bsd.port.mk>
