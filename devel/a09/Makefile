
COMMENT =		6800/6801/6809/6309/68HC11 Assembler 

DISTNAME =		a09-20201218
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/Arakula/A09

GH_ACCOUNT =		Arakula
GH_PROJECT =		A09
GH_COMMIT =		3d8e1486d100366d7b5f36b4146f9cab385ed404

WANTLIB +=		c

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/a09  ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/a09
			cp ${WRKSRC}/a09.htm ${PREFIX}/share/a09

.include <bsd.port.mk>
