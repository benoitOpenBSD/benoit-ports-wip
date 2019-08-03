# $OpenBSD$

COMMENT =		a cross-assembler targetting the C64

DISTNAME =		dreamass-20140504
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/docbacardi/dreamass

GH_ACCOUNT =		docbacardi
GH_PROJECT =		dreamass
GH_COMMIT =		ba43fe1a1cc038a617e6afc11363a72606e2f91e

WANTLIB +=		c

USE_GMAKE =		Yes

BUILD_DEPENDS =		print/texinfo

post-build:
		cd ${WRKSRC}/docs && ${GMAKE} && \
		rm history.texi && touch history.texi && \
		${GMAKE} dreamass.pdf
        
do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/dreamass ${PREFIX}/bin/
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/dreamass
		cp -R ${WRKSRC}/docs/*.{html,txt,info,pdf} ${PREFIX}/share/doc/dreamass

do-test:
		@cd ${WRKSRC}/test && ${GMAKE} all

.include <bsd.port.mk>
