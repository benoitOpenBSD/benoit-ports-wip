
COMMENT =		fork of byuu bass assembler 

DISTNAME =		bass-18.20220512
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ISC
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/ARM9/bass

GH_ACCOUNT =		ARM9
GH_PROJECT =		bass
GH_COMMIT =		c3962ec01f4768be1667db0d09c12141c28241f3

WANTLIB +=		${COMPILER_LIBCXX}
WANTLIB +=		c m pthread

USE_GMAKE =		Yes

do-build:
	cd ${WRKBUILD}/bass && ${GMAKE}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bass/out/bass ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/bass
	${INSTALL_DATA} ${WRKSRC}/doc/* ${PREFIX}/share/doc/bass	
	${INSTALL_DATA} ${WRKSRC}/bass/doc/bass.html ${PREFIX}/share/doc/bass
	${INSTALL_DATA_DIR} ${PREFIX}/share/bass/architectures
	cp -R ${WRKSRC}/bass/data/architectures/* ${PREFIX}/share/bass/architectures/
	
.include <bsd.port.mk>
