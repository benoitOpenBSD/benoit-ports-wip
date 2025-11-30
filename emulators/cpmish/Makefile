
COMMENT =		open source sort-of-CP/M distribution

DISTNAME =		cpmish-20251010
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/cpmish

GH_ACCOUNT =		davidgiven
GH_PROJECT =		cpmish
GH_COMMIT =		7f37cae18ca45b5338befec8b90db3663f44dc09

WANTLIB +=		c

USE_GMAKE =		Yes

# coreutils : ghead, gtruncate
BUILD_DEPENDS =		sysutils/cpmtools \
			sysutils/coreutils \
			devel/ack

NO_TEST =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/cpmish
			cp ${WRKSRC}/*.img ${PREFIX}/share/cpmish
			
.include <bsd.port.mk>
