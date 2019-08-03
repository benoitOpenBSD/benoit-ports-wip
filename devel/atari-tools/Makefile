# $OpenBSD$

COMMENT =		manipulate Atari 800 .ATR images

DISTNAME =		atari-tools-20180706
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv1
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/jhallen/atari-tools/

GH_ACCOUNT =		jhallen
GH_PROJECT =		atari-tools
GH_COMMIT =		3fcb836b548fde3994f53c14e8d100e96cc9b6e2

WANTLIB +=		c

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/atr2imd ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/imd2atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/detok ${PREFIX}/bin/

.include <bsd.port.mk>
