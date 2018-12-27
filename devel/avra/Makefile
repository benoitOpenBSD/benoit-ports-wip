# $OpenBSD$

COMMENT =		assembler for the Atmel AVR microcontroller family

V =			1.3.0
DISTNAME =		avra-${V}
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		https://sourceforge.net/projects/avra/files/${V}/

HOMEPAGE =		http://avra.sourceforge.net/index.html

EXTRACT_SUFX =		.tar.bz2

WANTLIB +=		c

NO_TEST =		Yes

do-build:
			cd ${WRKBUILD}/src && ${MAKE} -f makefiles/Makefile.osx

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/src/avra ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/avra/examples
		cp ${WRKSRC}/examples/* ${PREFIX}/share/avra/examples
		${INSTALL_DATA_DIR} ${PREFIX}/share/avra/includes
		cp ${WRKSRC}/includes/* ${PREFIX}/share/avra/includes

.include <bsd.port.mk>
