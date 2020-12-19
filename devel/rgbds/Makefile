# $OpenBSD$

COMMENT =		rednex Game Boy Development System

DISTNAME =		rgbds-0.4.2
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/rednex/rgbds

GH_ACCOUNT =		rednex
GH_PROJECT =		rgbds
GH_TAGNAME =		v0.4.2

WANTLIB +=		c m png z

LIB_DEPENDS =		graphics/png

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/rgbasm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbfix ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgbgfx ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/rgblink ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/src/asm/rgbasm.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/src/fix/rgbfix.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/src/gfx/rgbgfx.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/src/link/rgblink.1 ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/src/rgbds.5 ${PREFIX}/man/man5
	${INSTALL_MAN} ${WRKSRC}/src/rgbds.7 ${PREFIX}/man/man7
	${INSTALL_MAN} ${WRKSRC}/src/gbz80.7 ${PREFIX}/man/man7

.include <bsd.port.mk>
