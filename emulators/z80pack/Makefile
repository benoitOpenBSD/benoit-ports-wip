# $OpenBSD$

COMMENT =		a Zilog Z80 and Intel 8080 systems emulation

DISTNAME =		z80pack-1.36
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/udo-munk/z80pack

GH_ACCOUNT =		udo-munk
GH_PROJECT =		z80pack
GH_COMMIT =		aca63ff0164e292467a80572d97842214e607024

WANTLIB +=		c

#USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/z80pack-${GH_COMMIT}

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD}/z80asm && ${MAKE}
	cd ${WRKBUILD}/z80sim/srcsim && ${MAKE} -f Makefile.bsd

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/z80asm/z80asm ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKBUILD}/z80sim/srcsim/z80sim ${PREFIX}/bin/
#	${INSTALL_DATA_DIR} ${PREFIX}/include/cc65
#	cp -R ${WRKSRC}/include/* ${PREFIX}/include/cc65
#	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/samples
#	cp -R ${WRKSRC}/samples/* ${PREFIX}/share/cc65/samples

.include <bsd.port.mk>
