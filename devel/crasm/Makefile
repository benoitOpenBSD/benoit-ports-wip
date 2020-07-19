# $OpenBSD$

COMMENT =		portable cross-asm for the 6800,6801,6803,6502,65C02,Z80

DISTNAME =		crasm-1.9.20200526
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/colinbourassa/crasm

GH_ACCOUNT =		colinbourassa
GH_PROJECT =		crasm
GH_COMMIT =		a681595db2d2b99bc748f5013c9b5cecfb4f5bac

WANTLIB +=		c m

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/crasm ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/crasm.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
