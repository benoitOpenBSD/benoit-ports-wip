# $OpenBSD$

COMMENT =		Replacement for the arc program

DISTNAME =		nomarch-1.4
CATEGORIES =		archivers

#HOMEPAGE =		ftp://ftp.ibiblio.org/pub/Linux/utils/compress/
HOMEPAGE =		https://www.ibiblio.org/pub/Linux/utils/compress/

MAINTAINER =		Benoit Lecocq <blq@arcane-labs.net>

# GPLv2
PERMIT_PACKAGE =	Yes 

WANTLIB =		c

MASTER_SITES =		ftp://ftp.ibiblio.org/pub/Linux/utils/compress/ \
			ftp://sunsite.unc.edu/pub/Linux/utils/compress/

MAKE_FLAGS +=		CC="${CC}" LD="${CC}" CFLAGS="${CFLAGS}"

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/nomarch ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/nomarch.1 ${PREFIX}/man/man1/nomarch.1
                
.include <bsd.port.mk>
