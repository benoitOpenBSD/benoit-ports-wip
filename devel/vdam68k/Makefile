# $OpenBSD$

COMMENT =		portable M68k disasm for 68000-68060,68851,68881,68882

PKGNAME =		vdam68k-1.4
DISTNAME =      	vdam68k

CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Freeware
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://sun.hasenbraten.de/~frank/projects/download/ \
			http://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://sun.hasenbraten.de/~frank/projects/

WANTLIB +=		c

WRKSRC =		${WRKDIR}/vda/M68k

ALL_TARGET =		vda68k

MAKE_FLAGS =		CC="${CC}" COPTS="${CFLAGS} -D_ANSI_SOURCE"

NO_TEST =		Yes
	
do-install:
			${INSTALL_PROGRAM} ${WRKBUILD}/vda68k ${PREFIX}/bin

.include <bsd.port.mk>
