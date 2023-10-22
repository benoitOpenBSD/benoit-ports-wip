# $OpenBSD$

COMMENT =		asm for programming GAL devices

DISTNAME =		GALasm-2.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Commercial use is strictly forbidden
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/daveho/GALasm

# 2022/03/30
GH_ACCOUNT =		daveho
GH_PROJECT =		GALasm
GH_COMMIT =		290d0cf9dcd0d9749167c9019ad694db2c3360dd

WANTLIB +=		c

DEBUG_PACKAGES =	${BUILD_PACKAGES}

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD}/src && ${MAKE}

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/src/galasm ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/galasm/examples
	cp -R ${WRKSRC}/examples/* ${PREFIX}/share/galasm/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/galasm/galer
	cp -R ${WRKSRC}/galer/* ${PREFIX}/share/galasm/galer

.include <bsd.port.mk>
