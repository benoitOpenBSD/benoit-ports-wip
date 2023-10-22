
COMMENT =		disassembler for 6502 processors 

DISTNAME =		dcc6502-2.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE =	Yes

SITES =		        ${SITES_GITHUB}

HOMEPAGE =		https://github.com/tcarmelveilleux/dcc6502

GH_ACCOUNT =		tcarmelveilleux
GH_PROJECT =		dcc6502
GH_COMMIT =		680c21299241133449056c2ddfbc0dd087dc3807

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/dcc6502 ${PREFIX}/bin/

.include <bsd.port.mk>
