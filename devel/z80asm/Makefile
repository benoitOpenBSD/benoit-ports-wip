# $OpenBSD$

COMMENT =		assembler for the Z80 CPU

DISTNAME =		z80asm-1.8
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			http://download.savannah.nongnu.org/releases/z80asm/

HOMEPAGE =		http://savannah.nongnu.org/projects/z80asm/

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/z80asm ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/z80asm.1 ${PREFIX}/man/man1
	${INSTALL_DATA_DIR} ${PREFIX}/share/z80asm/examples
	cp -R ${WRKSRC}/examples/* ${PREFIX}/share/z80asm/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/z80asm/headers
	cp -R ${WRKSRC}/headers/* ${PREFIX}/share/z80asm/headers

.include <bsd.port.mk>
