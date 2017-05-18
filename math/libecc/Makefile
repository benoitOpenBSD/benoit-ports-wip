# $OpenBSD$

COMMENT =		library for elliptic curves cryptography

GH_COMMIT =		934a31ab20c4c52c0b50469ac6be32e72b5187f1
GH_ACCOUNT =		ANSSI-FR
GH_PROJECT =		libecc
DISTNAME =		libecc-0.20170517

CATEGORIES =		math

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Dual BSD / GPLv2
PERMIT_PACKAGE_CDROM =	Yes

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
