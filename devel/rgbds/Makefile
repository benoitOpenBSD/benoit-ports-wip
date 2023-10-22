COMMENT =		rednex Game Boy Development System

V =			0.6.1
DISTNAME =		rgbds-${V}
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://rgbds.gbdev.io/

SITES =			https://github.com/gbdev/rgbds/releases/download/v$V/

COMPILER =		ports-gcc
COMPILER_LANGS =	c c++

WANTLIB +=		c m png z

WRKDIST =		${WRKDIR}/rgbds

USE_GMAKE =		Yes

MAKE_FLAGS =		CFLAGS="${CFLAGS}" \
			CXXFLAGS="${CXXFLAGS}" \
			CXX="${CXX}" \
			BINMODE=${BINMODE} \
			MANMODE=${MANMODE} \
			Q=

LIB_DEPENDS =		graphics/png

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/rgbasm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbfix ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbgfx ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgblink ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/man/rgbasm.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/man/rgbfix.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/man/rgbgfx.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/man/rgblink.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/man/rgbds.5 ${PREFIX}/man/man5
	${INSTALL_MAN} ${WRKSRC}/man/rgbasm.5 ${PREFIX}/man/man5
	${INSTALL_MAN} ${WRKSRC}/man/rgblink.5 ${PREFIX}/man/man5
	${INSTALL_MAN} ${WRKSRC}/man/rgbds.7 ${PREFIX}/man/man7
	${INSTALL_MAN} ${WRKSRC}/man/gbz80.7 ${PREFIX}/man/man7

.include <bsd.port.mk>
