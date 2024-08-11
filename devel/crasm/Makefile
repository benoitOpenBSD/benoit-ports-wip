
COMMENT =		portable cross-asm for the 6800,6801,6803,6502,65C02,Z80

DISTNAME =		crasm-1.11.20230203
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/colinbourassa/crasm

GH_ACCOUNT =		colinbourassa
GH_PROJECT =		crasm
GH_COMMIT =		6cfbf5db046e8a176d83190c61c6e534e050997e

WANTLIB +=		c m

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/crasm ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/crasm.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
