# $OpenBSD$

COMMENT =		converting intel/motorola hexadecimal files to binary

DISTNAME =		Hex2bin-2.5
PKGNAME =		${DISTNAME:S/Hex2bin/hex2bin/}
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

HOMEPAGE =		http://hex2bin.sourceforge.net/

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=hex2bin/}

EXTRACT_SUFX =		.tar.bz2

WANTLIB +=		c

MAKE_FLAGS =		CC="${CC}" CFLAGS="${CFLAGS}"

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/hex2bin ${PREFIX}/bin/
	${INSTALL_PROGRAM} ${WRKSRC}/mot2bin ${PREFIX}/bin/
	${INSTALL_MAN} ${WRKSRC}/hex2bin.1 ${PREFIX}/man/man1

.include <bsd.port.mk>
