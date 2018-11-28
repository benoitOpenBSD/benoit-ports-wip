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
	cd ${WRKBUILD}/cpmsim/srctools && ${MAKE}
	cd ${WRKBUILD}/cpmsim/srcsim && ${MAKE} -f Makefile.bsd

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/z80pack/bin
	${INSTALL_PROGRAM} ${WRKBUILD}/z80asm/z80asm ${PREFIX}/z80pack/bin/z80asm
	${INSTALL_PROGRAM} ${WRKBUILD}/z80sim/srcsim/z80sim ${PREFIX}/z80pack/bin/
	${INSTALL_PROGRAM} \
		${WRKBUILD}/cpmsim/srctools/{bin2hex,mkdskimg,ptp2bin,receive,send} \
		${PREFIX}/z80pack/bin/
	${INSTALL_PROGRAM} ${WRKBUILD}/cpmsim/cpmsim ${PREFIX}/z80pack/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/z80pack/cpmsim/disks
	cp -R ${WRKSRC}/cpmsim/disks/* ${PREFIX}/z80pack/cpmsim/disks
	${INSTALL_DATA_DIR} ${PREFIX}/z80pack/cpmsim/conf
	cp -R ${WRKSRC}/cpmsim/conf/* ${PREFIX}/z80pack/cpmsim/conf
	${INSTALL_DATA_DIR} ${PREFIX}/z80pack/examples
	cp -R ${WRKSRC}/z80src/* ${PREFIX}/z80pack/examples
	${INSTALL_DATA_DIR} ${PREFIX}/z80pack/doc
	cp -R ${WRKSRC}/doc/* ${PREFIX}/z80pack/doc

.include <bsd.port.mk>
