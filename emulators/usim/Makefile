
COMMENT =		mc6809 emulator

DISTNAME =		usim-20210321
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MPL-2.0
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/raybellis/usim

GH_ACCOUNT =		raybellis
GH_PROJECT =		usim
GH_COMMIT =		419537dc7d3c64bc105987caa64c6b25be2aa418

WANTLIB +=		c ${COMPILER_LIBCXX}

ALL_TARGET =		usim

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/usim ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/usim
			${INSTALL_DATA} ${WRKSRC}/docs/* ${PREFIX}/share/usim
			${INSTALL_DATA} ${WRKSRC}/history/* ${PREFIX}/share/usim
			${INSTALL_DATA} ${WRKSRC}/tests/* ${PREFIX}/share/usim

NO_TEST =		Yes

.include <bsd.port.mk>
