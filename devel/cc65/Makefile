# $OpenBSD$

COMMENT =		a freeware C compiler for 6502 based systems

DISTNAME =		cc65-20160810
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# zlib
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://cc65.github.io/cc65/

GH_ACCOUNT =		cc65
GH_PROJECT =		cc65
GH_COMMIT =		22d1f1da1b481bafc7247f8e2531077a1cc34c20

WANTLIB +=		c m

USE_GMAKE =		Yes

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD} && env GIT_SHA=${GH_COMMIT} ${GMAKE} bin

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bin/* ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/include/cc65
	cp -R ${WRKSRC}/include/* ${PREFIX}/include/cc65
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/samples
	cp -R ${WRKSRC}/samples/* ${PREFIX}/share/cc65/samples

.include <bsd.port.mk>
