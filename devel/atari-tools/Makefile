
COMMENT =		manipulate Atari 800 .ATR images

DISTNAME =		atari-tools-20211022
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv1
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/jhallen/atari-tools/

GH_ACCOUNT =		jhallen
GH_PROJECT =		atari-tools
GH_COMMIT =		835d5a6fc1258921949fe92400adb789c398b9c3

WANTLIB +=		c

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/atr2imd ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/imd2atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/detok ${PREFIX}/bin/

.include <bsd.port.mk>
