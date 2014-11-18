# $OpenBSD$

COMMENT =		A UNIX tool for secure deletion

DISTNAME =		wipe-0.20
CATEGORIES =		security

HOMEPAGE =		http://lambda-diode.com/software/wipe

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c

MASTER_SITES =		http://lambda-diode.com/resources/wipe/

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

ALL_TARGET =		"OpenBSD"

NO_TEST =		Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/wipe ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/wipe.1 ${PREFIX}/man/man1/wipe.1
                
.include <bsd.port.mk>
