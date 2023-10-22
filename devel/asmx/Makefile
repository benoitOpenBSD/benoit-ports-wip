
COMMENT =		macro cross-assembler

DISTNAME =		asmx-2.0

CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# XXX A voir
PERMIT_PACKAGE =	Yes

SITES =			http://www.retrotechnology.com/memship/ \
			https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		http://www.retrotechnology.com/memship/asmx.html

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/asmx ${PREFIX}/bin
	${INSTALL_DATA_DIR} ${PREFIX}/share/asmx
	cp ${WRKSRC}/*.{txt,html} ${PREFIX}/share/asmx
	cp -R ${WRKSRC}/test ${PREFIX}/share/asmx

.include <bsd.port.mk>
