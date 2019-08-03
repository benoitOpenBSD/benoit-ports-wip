# $OpenBSD$

COMMENT =		a 1802 cross-assembler

DISTNAME =		a18-2.5.20180305
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/carangil/A18

GH_ACCOUNT =		carangil
GH_PROJECT =		A18
GH_COMMIT =		bde2a0b9c61c6dddc15517a9e55128a56932951a

WANTLIB +=		c

ALL_TARGET =		a18

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/a18 ${PREFIX}/bin/
	${INSTALL_DATA_DIR} ${PREFIX}/share/a18
	cp ${WRKSRC}/{a18.txt,README,*.asm} ${PREFIX}/share/a18

.include <bsd.port.mk>
