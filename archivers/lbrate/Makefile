
COMMENT =		extract/decompress CP/M LBR archives

DISTNAME =		lbrate-1.1
CATEGORIES =		archivers

HOMEPAGE =		http://freshmeat.sourceforge.net/projects/lbrate/

MAINTAINER =		Benoit Lecocq <blq@arcane-labs.net>

# GPLv2
PERMIT_PACKAGE =	Yes 

WANTLIB =		c

SITES =			ftp://ftp.ibiblio.org/pub/Linux/utils/compress/ 

MAKE_FLAGS +=		CC="${CC}" LD="${CC}" CFLAGS="${CFLAGS}"

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/lbrate ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/lbrate.1 ${PREFIX}/man/man1/lbrate.1
                
.include <bsd.port.mk>
