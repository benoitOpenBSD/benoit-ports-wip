# $OpenBSD$

COMMENT =		asm for programming GAL devices

DISTNAME =		GALasm-2.1-200121
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Commercial use is strictly forbidden
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/daveho/GALasm

GH_ACCOUNT =		daveho
GH_PROJECT =		GALasm
GH_COMMIT =		acee511cbd879791a4e8029edb27e141a8df90ce

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
