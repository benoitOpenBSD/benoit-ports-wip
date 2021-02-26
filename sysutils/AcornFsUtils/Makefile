# $OpenBSD$

COMMENT =		command-line utilities for Acorn 8-bit ADFS and DFS

DISTNAME =		AcornFsUtils-20210206
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ??
PERMIT_PACKAGE =	Yes

MASTER_SITES =		https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		https://github.com/SteveFosdick/AcornFsUtils

WANTLIB +=		c zip

LIB_DEPENDS =		archivers/libzip>=0.11.2

MAKE_FLAGS =		CFLAGS="${CFLAGS} -I/usr/local/include" \
			LDFLAGS="${LDFLAGS} -L/usr/local/lib"
   
WRKDIST =		${WRKDIR}/AcornFsUtils

DEBUG_PACKAGES =	${BUILD_PACKAGES}

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/afsls ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afstree ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afscp ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afschk ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afstitle ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/acunzip ${PREFIX}/bin

.include <bsd.port.mk>
