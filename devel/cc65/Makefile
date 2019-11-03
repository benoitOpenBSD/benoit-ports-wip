# $OpenBSD$

COMMENT =		a freeware C compiler for 6502 based systems

DISTNAME =		cc65-20191101
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# zlib
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://cc65.github.io/cc65/

GH_ACCOUNT =		cc65
GH_PROJECT =		cc65
GH_COMMIT =		0d21a2b5a4a71a39b730492068ca1cf01448b4d5

WANTLIB +=		c m

USE_GMAKE =		Yes

NO_TEST =		Yes
	
do-build:
	cd ${WRKBUILD} && env GIT_SHA=${GH_COMMIT} ${GMAKE} bin lib

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bin/* ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/include
	cp -R ${WRKSRC}/include/* ${PREFIX}/share/cc65/include
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/samples
	cp -R ${WRKSRC}/samples/* ${PREFIX}/share/cc65/samples
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/lib
	cp -R ${WRKSRC}/lib/* ${PREFIX}/share/cc65/lib
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/target
	cp -R ${WRKSRC}/target/* ${PREFIX}/share/cc65/target
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/cfg
	cp -R ${WRKSRC}/cfg/* ${PREFIX}/share/cc65/cfg
	${INSTALL_DATA_DIR} ${PREFIX}/share/cc65/asminc
	cp -R ${WRKSRC}/asminc/* ${PREFIX}/share/cc65/asminc

.include <bsd.port.mk>
