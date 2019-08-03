# $OpenBSD$

COMMENT =	portable 6502 assembler with BBC Micro style syntax

V =		1.09
DISTNAME =	beebasm-${V}
CATEGORIES =	devel

HOMEPAGE =	https://github.com/stardot/beebasm

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

WANTLIB +=		c m ${COMPILER_LIBCXX}

MASTER_SITES =          ${MASTER_SITES_GITHUB}
GH_ACCOUNT =            stardot
GH_PROJECT =            beebasm
GH_TAGNAME =            v$V

COMPILER =		base-clang ports-gcc base-gcc

USE_GMAKE =		Yes

do-build:
		cd ${WRKBUILD}/src && exec ${SETENV} ${MAKE_ENV} MAKE=${GMAKE} \
		${GMAKE} code PLATFORM=linux

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/beebasm ${PREFIX}/bin/
		${INSTALL_DATA_DIR} ${PREFIX}/share/beebasm/examples
		cp -R ${WRKSRC}/examples/* ${PREFIX}/share/beebasm/examples
		cp ${WRKSRC}/*.6502 ${PREFIX}/share/beebasm/examples
		${INSTALL_DATA_DIR} ${PREFIX}/share/beebasm/docs
		cp ${WRKSRC}/README.md ${PREFIX}/share/beebasm/docs

do-test:
		cd ${WRKBUILD}/src && exec ${SETENV} ${MAKE_ENV} MAKE=${GMAKE} \
		${GMAKE} run PLATFORM=linux

.include <bsd.port.mk>
