# $OpenBSD$

COMMENT =		the dillon dasm macro assembler

DISTNAME =		dasm-2.20.14.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://dasm-assembler.github.io/

GH_ACCOUNT =            dasm-assembler
GH_PROJECT =            dasm
GH_TAGNAME =		2.20.14.1

WANTLIB +=		c

WRKDIST=		${WRKDIR}/${PKGNAME}

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bin/* ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/dasm
	${INSTALL_MAN} ${WRKSRC}/docs/*.txt ${PREFIX}/share/doc/dasm
	${INSTALL_DATA} ${WRKSRC}/docs/dasm.pdf $(PREFIX)/share/doc/dasm
	${INSTALL_DATA} ${WRKSRC}/docs/sources/images/illegal.png $(PREFIX)/share/doc/dasm/images

.include <bsd.port.mk>
