# $OpenBSD$

COMMENT =		highly configurable DNS proxy

MODPY_EGG_VERSION =	0.3
DISTNAME =		dnschef-${MODPY_EGG_VERSION}
CATEGORIES =		net

HOMEPAGE =		https://thesprawl.org/projects/dnschef/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		https://thesprawl.org/media/projects/
EXTRACT_SUFX =		.zip

MODULES =		lang/python

# Need to import py-dnslib 
RUN_DEPENDS =		net/py-dnslib \
			net/py-IP
BUILD_DEPENDS =		${RUN_DEPENDS}

NO_BUILD =		Yes
NO_TEST =		Yes

pre-configure:
	 cd ${WRKSRC}; perl -pi -e 's,/usr/bin/env python,${MODPY_BIN},;' dnschef.py

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/dnschef
	${INSTALL_SCRIPT} ${WRKSRC}/dnschef.py ${PREFIX}/bin
	${INSTALL_DATA} ${WRKSRC}/{CHANGELOG,LICENSE,README,TODO} ${PREFIX}/share/doc/dnschef

.include <bsd.port.mk>
