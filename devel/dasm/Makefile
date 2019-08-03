# $OpenBSD$

COMMENT =		the dillon dasm macro assembler

PKGNAME =		dasm-2.20.11
DISTNAME =		dasm-2.20.11-2014.03.04-source
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		http://dasm-dillon.sourceforge.net/

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=dasm-dillon/}

WANTLIB +=		c

WRKSRC =		${WRKDIR}/dasm-2.20.11-20140304
WRKDIST =		${WRKSRC}

USE_GMAKE =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bin/* ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/doc/dasm.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
