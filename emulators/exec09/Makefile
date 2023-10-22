
COMMENT =		6809 emulator

DISTNAME =		exec09-20090722
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/bcd/exec09

GH_ACCOUNT =		bcd
GH_PROJECT =		exec09
GH_COMMIT =		642e684b9d225a6d0a3d7121ed23ba79c76b9fc5

WANTLIB +=		c

AUTOCONF_VERSION =	2.69
AUTOMAKE_VERSION =	1.16

CONFIGURE_STYLE =	autoreconf

USE_GMAKE =		Yes

DEBUG_PACKAGES =	${BUILD_PACKAGES}


do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/m6809-run ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
