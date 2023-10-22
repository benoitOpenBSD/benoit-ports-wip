
COMMENT =	linker for .rel object files

DISTNAME =	ld80-0.6.1
CATEGORIES =	devel

HOMEPAGE =	http://48k.ca/ld80.html

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Public Domain
PERMIT_PACKAGE =	Yes

WANTLIB +=	${COMPILER_LIBCXX} c

# http://48k.ca/
SITES =		https://www.arcane-labs.net/download/OpenBSD/

COMPILER =	base-clang ports-gcc

ALL_TARGET =	ld80

NO_TEST =	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/ld80 ${PREFIX}/bin
	${INSTALL_MAN_DIR} ${PREFIX}/man/man1
	${INSTALL_MAN} ${WRKSRC}/ld80.1 ${PREFIX}/man/man1

DEBUG_PACKAGES =	${BUILD_PACKAGES}

.include <bsd.port.mk>
