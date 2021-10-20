# $OpenBSD$

COMMENT =		Lennart Benschop 6809 Single Board Computer

DISTNAME =		sbc09-20210623
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/6809/sbc09

GH_ACCOUNT =		6809
GH_PROJECT =		sbc09
GH_COMMIT =		4b772ecfe0c04e7b752d20d57359849b0a8aa781

WANTLIB +=		c

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/src

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/a09 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/{v09,v09s,v09st} ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
