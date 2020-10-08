# $OpenBSD$

COMMENT =		C64 music debug output utility

DISTNAME =		siddump-20201004
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/cadaver/siddump

GH_ACCOUNT =		cadaver
GH_PROJECT =		siddump
GH_COMMIT =		ef58ac47edcf35e6ef09aa17b5c23ea4bb9a079d

WANTLIB +=		c m

USE_GMAKE =		Yes
ALL_TARGET =		siddump

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/siddump ${PREFIX}/bin/

.include <bsd.port.mk>
