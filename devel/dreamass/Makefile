# $OpenBSD$

COMMENT =		a cross-assembler targetting the C64

DISTNAME =		dreamass-20140504
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/docbacardi/dreamass

GH_ACCOUNT =		docbacardi
GH_PROJECT =		dreamass
GH_COMMIT =		ba43fe1a1cc038a617e6afc11363a72606e2f91e

WANTLIB +=		c

USE_GMAKE =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/dreamass ${PREFIX}/bin/

do-test:
		@cd ${WRKSRC}/test && ${GMAKE} all

.include <bsd.port.mk>
