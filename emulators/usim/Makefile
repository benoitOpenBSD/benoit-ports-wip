# $OpenBSD$

COMMENT =		mc6809 emulator

DISTNAME =		usim-20200629
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MPL-2.0
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/raybellis/usim

GH_ACCOUNT =		raybellis
GH_PROJECT =		usim
GH_COMMIT =		c49c2ede11daccbf32f3c1066233a3ca28b82be6

WANTLIB +=		c ${COMPILER_LIBCXX}

ALL_TARGET =		usim

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/usim ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/usim
			${INSTALL_DATA} ${WRKSRC}/doc/* ${PREFIX}/share/usim
			${INSTALL_DATA} ${WRKSRC}/bin/* ${PREFIX}/share/usim

NO_TEST =		Yes

.include <bsd.port.mk>
