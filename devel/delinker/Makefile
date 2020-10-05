# $OpenBSD$

COMMENT =		Unlinks a binary executable to get back a set of .o files

DISTNAME =		delinker-20200306
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# ???
PERMIT_PACKAGE =	Yes

#MASTER_SITES =		${MASTER_SITES_GITHUB}
MASTER_SITES =          https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		https://github.com/jnider/delinker

#GH_ACCOUNT =		jnider
#GH_PROJECT =		delinker
#GH_COMMIT =		47ed3c890e947d451939d61d1fb95464a5579c35

WANTLIB +=		c

WRKDIST=	${WRKDIR}/delinker

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/delinker ${PREFIX}/bin/


.include <bsd.port.mk>
