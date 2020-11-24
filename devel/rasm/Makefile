# $OpenBSD$

COMMENT =		Yes Another Z80 assembler

DISTNAME =		rasm-20201123
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/EdouardBERGE/rasm

GH_ACCOUNT =		EdouardBERGE
GH_PROJECT =		rasm
GH_COMMIT =		f35148150c789dc611117e00a2b7ec9f6d302cd2

WANTLIB +=		c m

USE_GMAKE =		Yes
MAKE_FILE =		makefile

ALL_TARGET =		prod

DEBUG_PACKAGES =	${BUILD_PACKAGES}

NO_TEST =		Yes
	
do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/rasm ${PREFIX}/bin/
		${INSTALL_DATA_DIR} ${PREFIX}/share/rasm/decrunch
		cp -R ${WRKSRC}/decrunch/* ${PREFIX}/share/rasm/decrunch

.include <bsd.port.mk>
