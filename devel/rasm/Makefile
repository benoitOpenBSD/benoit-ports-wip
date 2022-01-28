# $OpenBSD$

COMMENT =		Yes Another Z80 assembler

DISTNAME =		rasm-20220127
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/EdouardBERGE/rasm

GH_ACCOUNT =		EdouardBERGE
GH_PROJECT =		rasm
GH_COMMIT =		fac4be2a04ad6e52c1c6d081464bbecc4c026dfd

WANTLIB +=		c m

USE_GMAKE =		Yes
MAKE_FILE =		makefile

ALL_TARGET =		prod

# DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/rasm ${PREFIX}/bin/
		${INSTALL_DATA_DIR} ${PREFIX}/share/rasm/decrunch
		cp -R ${WRKSRC}/decrunch/* ${PREFIX}/share/rasm/decrunch

do-test:
		cd ${WRKSRC} && ./rasm -autotest

.include <bsd.port.mk>
