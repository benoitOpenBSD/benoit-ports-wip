# $OpenBSD$

COMMENT =		manipulate Atari 800 .ATR images

DISTNAME =		atari-tools-20161007
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv1
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/jhallen/atari-tools/

GH_ACCOUNT =		jhallen
GH_PROJECT =		atari-tools
GH_COMMIT =		5aa49f4a9654d6beb1e7e6791bec3915c9145f61

WANTLIB +=		c

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/atr2imd ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/imd2atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/detok ${PREFIX}/bin/

.include <bsd.port.mk>
