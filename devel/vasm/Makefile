# $OpenBSD$

COMMENT =		portable and retargetable assembler

PKGNAME =		vasm-1.8d
DISTNAME =      	vasm1_8d

CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX A voir
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://server.owl.de/~frank/tags/ \
			http://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://sun.hasenbraten.de/vasm/index.php?view=main

WANTLIB +=		c m

USE_GMAKE =		Yes

# gmake CPU=m68k SYNTAX=mot
MAKE_ENV +=		CPU=m68k SYNTAX=mot

WRKDIST =       ${WRKDIR}/vasm

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/vasmm68k_mot ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKBUILD}/vobjdump ${PREFIX}/bin

.include <bsd.port.mk>
