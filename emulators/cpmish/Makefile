
COMMENT =		open source sort-of-CP/M distribution

DISTNAME =		cpmish-20240107
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/cpmish

GH_ACCOUNT =		davidgiven
GH_PROJECT =		cpmish
GH_COMMIT =		7c8d636efed47558c607831f64228e6ae18a0068

WANTLIB +=		c

# coreutils : ghead, gtruncate
BUILD_DEPENDS =		sysutils/cpmtools \
			sysutils/coreutils \
			devel/ack

NO_TEST =		Yes

do-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/cpmish
			cp ${WRKSRC}/*.img ${PREFIX}/share/cpmish
			
.include <bsd.port.mk>
