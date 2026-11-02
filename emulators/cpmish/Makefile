
COMMENT =		open source sort-of-CP/M distribution

DISTNAME =		cpmish-20260817
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/cpmish

GH_ACCOUNT =		davidgiven
GH_PROJECT =		cpmish
GH_COMMIT =		1f60541b619c1e983f05e68a064c027d1cdeb113

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
