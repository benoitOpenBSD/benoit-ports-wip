# $OpenBSD$

COMMENT =		open source sort-of-CP/M distribution

DISTNAME =		cpmish-20210105
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/davidgiven/cpmish

GH_ACCOUNT =		davidgiven
GH_PROJECT =		cpmish
GH_COMMIT =		f68ff8723a2bf172b84f66dfa89775e570a77993

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
