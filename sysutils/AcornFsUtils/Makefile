# $OpenBSD$

COMMENT =		command-line utilities for Acorn 8-bit ADFS and DFS

DISTNAME =		AcornFsUtils-20191107
CATEGORIES =		sysutils

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ??
PERMIT_PACKAGE =	Yes

MASTER_SITES =		https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		https://github.com/SteveFosdick/AcornFsUtils

WANTLIB +=		c

WRKDIST =		${WRKDIR}/AcornFsUtils

DEBUG_PACKAGES =	${BUILD_PACKAGES}

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/afsls ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afstree ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afscp ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/afschk ${PREFIX}/bin

.include <bsd.port.mk>
