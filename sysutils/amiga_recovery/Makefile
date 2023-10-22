
COMMENT =	view and copy files from Amiga file system images

V =		210425
DISTNAME =	amiga_recovery-${V}
CATEGORIES =	sysutils

HOMEPAGE =	https://github.com/mikeakohn/amiga_recovery

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =            mikeakohn
GH_PROJECT =            amiga_recovery
GH_COMMIT =		7a5157c742143dd07692121cbe116ffea819cfff

WANTLIB +=		c

USE_GMAKE =		Yes
ALL_TARGET =		default tools

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/amiga_recovery ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKSRC}/find_root_block ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKSRC}/find_partitions ${PREFIX}/bin
		${INSTALL_PROGRAM} ${WRKSRC}/parse_hunk ${PREFIX}/bin

NO_TEST =		Yes

.include <bsd.port.mk>
