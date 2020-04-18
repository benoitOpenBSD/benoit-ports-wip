# $OpenBSD$

COMMENT =		the dillon dasm macro assembler

DISTNAME =		dasm-2.20.14
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://dasm-assembler.github.io/

GH_ACCOUNT =            dasm-assembler
GH_PROJECT =            dasm
GH_COMMIT =		275e257f7f051d88aa52951c9fe38815d3180b46

WANTLIB +=		c

WRKSRC =		${WRKDIR}/dasm-${GH_COMMIT}
WRKDIST =		${WRKSRC}

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bin/* ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/dasm/doc
	${INSTALL_MAN} ${WRKSRC}/doc/*.txt ${PREFIX}/share/dasm/doc

.include <bsd.port.mk>
