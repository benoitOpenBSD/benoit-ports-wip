# $OpenBSD$

COMMENT =		asm for programming GAL devices

DISTNAME =		GALasm-2.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Commercial use is strictly forbidden
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/daveho/GALasm

# 2020/10/22
GH_ACCOUNT =		daveho
GH_PROJECT =		GALasm
GH_COMMIT =		1fa74e520715e1a99fcb03ad8683b8b266ced6db

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
