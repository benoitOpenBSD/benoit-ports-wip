# $OpenBSD$

COMMENT =		disassembler for 6502 processors 

DISTNAME =		dcc6502-2.1
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# MIT
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/tcarmelveilleux/dcc6502

GH_ACCOUNT =		tcarmelveilleux
GH_PROJECT =		dcc6502
GH_COMMIT =		c003395dd7ab054340e88960515e22228e86d32a

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/dcc6502 ${PREFIX}/bin/

.include <bsd.port.mk>
