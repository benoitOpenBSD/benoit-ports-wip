
COMMENT =		a Microchip PIC disassembler

DISTNAME =		vpicdidasm-20180404
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/vsergeev/vpicdisasm

GH_ACCOUNT =		vsergeev
GH_PROJECT =		vpicdisasm
GH_COMMIT =		8350f9ecdf8b2086c67d9b4ba2fbae675c36d8f3

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/vpicdisasm
	cp ${WRKSRC}/README ${PREFIX}/share/doc/vpicdisasm
	cp ${WRKSRC}/disasm_flow.txt ${PREFIX}/share/doc/vpicdisasm

.include <bsd.port.mk>
