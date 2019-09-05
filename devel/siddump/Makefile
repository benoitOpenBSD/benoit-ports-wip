# $OpenBSD$

COMMENT =		C64 music debug output utility

DISTNAME =		siddump-20190814
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/cadaver/siddump

GH_ACCOUNT =		cadaver
GH_PROJECT =		siddump
GH_COMMIT =		7264a4ff20d98f0ace1d98dae47800199c415def

WANTLIB +=		c m

# XXX Makefile to re-create
USE_GMAKE =		Yes
MAKE_FILE =		makefile
ALL_TARGET =		siddump

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/siddump ${PREFIX}/bin/

.include <bsd.port.mk>
