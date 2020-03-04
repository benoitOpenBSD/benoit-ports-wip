# $OpenBSD$

COMMENT =		portable M68k disasm for 68000-68060,68851,68881,68882

DISTNAME =		vdam68k-1.5
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Freeware
PERMIT_PACKAGE =	Yes

MASTER_SITES =		http://sun.hasenbraten.de/~frank/projects/download/ \
			https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://sun.hasenbraten.de/~frank/projects/

WANTLIB +=		c

WRKSRC =		${WRKDIR}/vda/M68k

ALL_TARGET =		vda68k

MAKE_FLAGS =		CC="${CC}" COPTS="${CFLAGS} -D_ANSI_SOURCE"

NO_TEST =		Yes
	
do-install:
			${INSTALL_PROGRAM} ${WRKBUILD}/vda68k ${PREFIX}/bin

.include <bsd.port.mk>
