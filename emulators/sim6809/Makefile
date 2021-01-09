# $OpenBSD$

COMMENT =		6809 emulator

DISTNAME =		sim6809-20160708
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/gordonjcp/sim6809

GH_ACCOUNT =		gordonjcp
GH_PROJECT =		sim6809
GH_COMMIT =		da56d8c1ea14d2aa8fad8934e6abb7c57ebf81f5

WANTLIB +=		c util

AUTOCONF_VERSION =	2.69
AUTOMAKE_VERSION =	1.16

CONFIGURE_STYLE =	autoreconf

USE_GMAKE =		Yes

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/emu/sim6809 ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/sim6809
			${INSTALL_DATA} ${WRKSRC}/doc/* ${PREFIX}/share/sim6809
			${INSTALL_DATA} ${WRKSRC}/README ${PREFIX}/share/sim6809

NO_TEST =		Yes

.include <bsd.port.mk>
