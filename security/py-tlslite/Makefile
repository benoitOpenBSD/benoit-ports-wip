# $OpenBSD$

COMMENT =		python library that implements SSL 3.0, TLS 1.0, and TLS 1.1

MODPY_EGG_VERSION =	0.3.8
DISTNAME =		tlslite-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		security

HOMEPAGE =		http://trevp.net/tlslite/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Public domain
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://trevp.net/tlslite/

MODULES =		lang/python

NO_REGRESS =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/py-tlslite
	${INSTALL_DATA} ${WRKSRC}/readme.txt ${PREFIX}/share/doc/py-tlslite
	        
.include <bsd.port.mk>
