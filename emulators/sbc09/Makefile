
COMMENT =		Lennart Benschop 6809 Single Board Computer

DISTNAME =		sbc09-20220111
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/6809/sbc09

GH_ACCOUNT =		6809
GH_PROJECT =		sbc09
GH_COMMIT =		39181b46a058fe23f6606ee2fe5e6d237f7d4ba0

WANTLIB +=		c

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/src

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/a09 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/{v09,v09s,v09st} ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
