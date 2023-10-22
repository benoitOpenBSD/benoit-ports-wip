
COMMENT =		open source sort-of-CP/M distribution

DISTNAME =		cpmish-20220712
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/cpmish

GH_ACCOUNT =		davidgiven
GH_PROJECT =		cpmish
GH_COMMIT =		d3db03d399bfbf5afd38067bcad0f8b2afe9c9e6

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
