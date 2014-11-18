# $OpenBSD$

COMMENT =		python library that implements SSL 3.0, TLS 1.0, and TLS 1.1

MODPY_EGG_VERSION =	0.4.3
DISTNAME =		tlslite-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		security

HOMEPAGE =		http://trevp.net/tlslite/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Public domain and BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=t/tlslite/}

MODULES =		lang/python

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/py-tlslite
	${INSTALL_DATA} ${WRKSRC}/README ${PREFIX}/share/doc/py-tlslite
	${INSTALL_DATA} ${WRKSRC}/docs/* ${PREFIX}/share/doc/py-tlslite
	        
.include <bsd.port.mk>
