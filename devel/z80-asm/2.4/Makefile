# $OpenBSD$

COMMENT =		assembler and monitor for the Z80 CPU

DISTNAME =		z80-asm-current
PKGNAME =		z80-asm-2.4.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		http://wwwhomes.uni-bielefeld.de/achim/z80-asm/

HOMEPAGE =		http://wwwhomes.uni-bielefeld.de/achim/z80-asm.html

WANTLIB +=		c

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/z80-asm-2.4.1

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/z80-asm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/z80-mon ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/doc/man/*.1 ${PREFIX}/man/man1
	${INSTALL_DATA_DIR} ${PREFIX}/share/z80-asm/examples
	cp -R ${WRKSRC}/programs/* ${PREFIX}/share/z80-asm/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/z80-asm
	cp -R ${WRKSRC}/doc/*.{html,txt,ps} ${PREFIX}/share/doc/z80-asm

.include <bsd.port.mk>
