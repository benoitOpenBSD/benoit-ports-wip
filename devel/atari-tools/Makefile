# $OpenBSD$

COMMENT =		manipulate Atari 800 .ATR images

DISTNAME =		atari-tools-20180418
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv1
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/jhallen/atari-tools/

GH_ACCOUNT =		jhallen
GH_PROJECT =		atari-tools
GH_COMMIT =		ec5812343b19166d4139b9ae7c15756ae4d8f26b

WANTLIB +=		c

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/atr2imd ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/imd2atr ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/detok ${PREFIX}/bin/

.include <bsd.port.mk>
