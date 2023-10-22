
COMMENT =		a mostly Mac/65 compatible cross-assembler

PKGNAME =		atasm-1.09
DISTNAME =		atasm109
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${HOMEPAGE}

HOMEPAGE =		http://atari.miribilist.com/atasm/

EXTRACT_SUFX=		.zip

WANTLIB +=		c z

USE_GMAKE =		Yes

WRKSRC =                ${WRKDIR}/atasm109
WRKDIST =               ${WRKSRC}

do-build:
	cd ${WRKBUILD}/src && ${GMAKE}

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/atasm ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/atasm/examples
	cp -R ${WRKSRC}/examples/* ${PREFIX}/share/atasm/examples
	${INSTALL_DATA_DIR} ${PREFIX}/share/atasm/docs
	cp -R ${WRKSRC}/docs/* ${PREFIX}/share/atasm/docs

do-test:
	cd ${WRKSRC}/tests && ${GMAKE}

.include <bsd.port.mk>
