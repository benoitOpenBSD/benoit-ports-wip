
COMMENT =	tool to show information about a running OpenBSD system

DISTNAME =	bsdfetch-230110
CATEGORIES =	sysutils

HOMEPAGE =	https://github.com/jhx0/bsdfetch

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# ISC
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =		jhx0
GH_PROJECT =		bsdfetch
GH_COMMIT =		644b1a54b7103307592c1ff67b3f9f641eaa437b

NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKBUILD}/bsdfetch ${PREFIX}/bin
		
.include <bsd.port.mk>
