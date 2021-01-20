# $OpenBSD$

COMMENT =		680x/630x Disassembler

DISTNAME =		f9dasm-20210118
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/Arakula/f9dasm

GH_ACCOUNT =		Arakula
GH_PROJECT =		f9dasm
GH_COMMIT =		13327c3cbbcc97496da0ef3ce5c5f98bf41343af

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/f9dasm  ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/hex2bin ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/mot2bin ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/f9dasm
			cp ${WRKSRC}/f9dasm.htm ${PREFIX}/share/f9dasm
			cp ${WRKSRC}/sample.zip ${PREFIX}/share/f9dasm
			

.include <bsd.port.mk>
