# $OpenBSD$

COMMENT =	tool to show information about a running OpenBSD system

DISTNAME =	bsdfetch-221116
CATEGORIES =	sysutils

HOMEPAGE =	https://github.com/jhx0/bsdfetch

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# ISC
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =		jhx0
GH_PROJECT =		bsdfetch
GH_COMMIT =		c3a64934fe17d8753009c636d114178ad96c2789

NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/bsdfetch ${PREFIX}/bin
		
.include <bsd.port.mk>
