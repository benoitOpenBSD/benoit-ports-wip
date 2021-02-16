# $OpenBSD$

COMMENT =		portable cross-asm for the 6800,6801,6803,6502,65C02,Z80

DISTNAME =		crasm-1.9.20210216
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/colinbourassa/crasm

GH_ACCOUNT =		colinbourassa
GH_PROJECT =		crasm
GH_COMMIT =		932f3293f96f36bfe32f8d8d70a5ba693d3b3193

WANTLIB +=		c m

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/crasm ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/crasm.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
