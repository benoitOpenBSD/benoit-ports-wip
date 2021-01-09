# $OpenBSD$

COMMENT =		Lennart Benschop 6809 Single Board Computer

DISTNAME =		sbc09-20200209
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/6809/sbc09

GH_ACCOUNT =		6809
GH_PROJECT =		sbc09
GH_COMMIT =		21aa3bc6ff840ed1a14b8a49f80740137f59593d

WANTLIB +=		c

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/src

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/a09 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/{v09,v09s,v09st} ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
