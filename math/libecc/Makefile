# $OpenBSD$

COMMENT =		library for elliptic curves cryptography

GH_COMMIT =		4c1d5afde0c05c74ffafdba2fa4c6653dfb33b36
GH_ACCOUNT =		ANSSI-FR
GH_PROJECT =		libecc
DISTNAME =		libecc-0.20200516

CATEGORIES =		math

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Dual BSD / GPLv2
PERMIT_PACKAGE =	Yes

USE_GMAKE =		Yes

# XXX need to include *.h file
do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/build/ec_self_tests ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKSRC}/build/ec_utils ${PREFIX}/bin
		${INSTALL_DATA} ${WRKSRC}/build/libarith.a ${PREFIX}/lib
		${INSTALL_DATA} ${WRKSRC}/build/libec.a ${PREFIX}/lib
		${INSTALL_DATA} ${WRKSRC}/build/libsign.a ${PREFIX}/lib

NO_TEST =		Yes

.include <bsd.port.mk>
