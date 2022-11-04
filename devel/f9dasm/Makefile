# $OpenBSD$

COMMENT =		680x/630x Disassembler

DISTNAME =		f9dasm-20221007
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/Arakula/f9dasm

GH_ACCOUNT =		Arakula
GH_PROJECT =		f9dasm
GH_COMMIT =		1c7c88e320d427fa9a6a7edb6aa60370a106e9cf

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
