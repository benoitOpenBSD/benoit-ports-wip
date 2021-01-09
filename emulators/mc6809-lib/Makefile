# $OpenBSD$

COMMENT =		6809 emulator library

DISTNAME =		mc6809-lib-20200528
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv3
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/spc476/mc6809

GH_ACCOUNT =		spc476
GH_PROJECT =		mc6809
GH_COMMIT =		9944689179c50719fe34645f06104e9dde7e6fb5

WANTLIB +=		c

USE_GMAKE =		Yes

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/mc09emulator ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/mc09disasm ${PREFIX}/bin/
			${INSTALL_DATA} ${WRKSRC}/libmc6809.a ${PREFIX}/lib
			${INSTALL_DATA} ${WRKSRC}/{mc6809,mc6809dis}.h ${PREFIX}/include

NO_TEST =		Yes

.include <bsd.port.mk>
