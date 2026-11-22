# $OpenBSD$

COMMENT =	cross-platform table-driven cross-assembler

V =		3.1
DISTNAME =	rcasm-${V}
CATEGORIES =	devel

# http://www.elf-emulation.com/rcasm.html
HOMEPAGE =	${SITES_GITHUB}

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Freeware ?
PERMIT_PACKAGE =	Yes

WANTLIB +=		c

# https://www.arcane-labs.net/download/OpenBSD/
GH_ACCOUNT =            rileym65
GH_PROJECT =            RcAsm
GH_COMMIT =             3fb25223547274da0c9d9e3e5f35cb5f58e0f343

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/{rcasm,rclink} ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/rcasm/doc
	cp ${WRKSRC}/{asm.doc,*.def,*.txt} ${PREFIX}/share/rcasm/doc

NO_TEST =	Yes

.include <bsd.port.mk>
