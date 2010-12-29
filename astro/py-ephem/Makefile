# $OpenBSD$

COMMENT =		Astronomical computations for Python

MODPY_EGG_VERSION =	3.7.3.4
DISTNAME =		pyephem-${MODPY_EGG_VERSION}
PKGNAME =		py-ephem-${MODPY_EGG_VERSION}
CATEGORIES =		astro

HOMEPAGE =		http://rhodesmill.org/pyephem/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3 - LGPLv3
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=p/pyephem/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

DOCSDIR =       ${PREFIX}/share/doc/py-ephem

post-install:
		${INSTALL_DATA_DIR} ${DOCSDIR}
		${INSTALL_SCRIPT} ${WRKSRC}/src/ephem/doc/* ${DOCSDIR}
 
.include <bsd.port.mk>
