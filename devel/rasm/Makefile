# $OpenBSD$

COMMENT =		Yes Another Z80 assembler

DISTNAME =		rasm-20211112
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/EdouardBERGE/rasm

GH_ACCOUNT =		EdouardBERGE
GH_PROJECT =		rasm
GH_COMMIT =		96f1cfb1adf2e0c967c3800128ff3b25792ebde9

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
