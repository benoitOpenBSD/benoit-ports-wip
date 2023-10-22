
COMMENT =		emulator core for MC6809E processor

DISTNAME =		6809_core-20180209
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/episcopus/6809_core

GH_ACCOUNT =		episcopus
GH_PROJECT =		6809_core
GH_COMMIT =		8e7a3cc4efaf4e6f9fd80fcb8250811be97f53c2

WANTLIB +=		c

BUILD_DEPENDS +=	graphics/png

USE_GMAKE =		Yes
MAKE_FILE =		makefile

pre-configure:
			mkdir ${WRKSRC}/build
do-install:
			${INSTALL_DATA} ${WRKSRC}/build/6809.a ${PREFIX}/lib

NO_TEST =		Yes

.include <bsd.port.mk>
