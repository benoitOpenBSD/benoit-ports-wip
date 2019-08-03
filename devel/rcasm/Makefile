# $OpenBSD$

COMMENT =	cross-platform table-driven cross-assembler

V =		3.0
DISTNAME =	rcasm-${V}
CATEGORIES =	devel

HOMEPAGE =	http://www.elf-emulation.com/rcasm.html

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Freeware ?
PERMIT_PACKAGE =	Yes

WANTLIB +=		c

MASTER_SITES =		http://www.arcane-labs.net/download/OpenBSD/

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/{rcasm,rclink} ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/rcasm/doc
	cp ${WRKSRC}/{asm.doc,*.def,*.txt} ${PREFIX}/share/rcasm/doc

NO_TEST =	Yes

.include <bsd.port.mk>
