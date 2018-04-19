# $OpenBSD$

COMMENT =		portable cross-asm for the 6800,6801,6803,6502,65C02,Z80

DISTNAME =		crasm-1.9.20171014
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/colinbourassa/crasm

GH_ACCOUNT =		colinbourassa
GH_PROJECT =		crasm
GH_COMMIT =		e1e7ccc2f4b590c33a981436a54504db747b449d

WANTLIB +=		c m

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/crasm ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/crasm.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
