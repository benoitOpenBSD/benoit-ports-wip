# $OpenBSD$

COMMENT =		a Z80 cross assembler from Mark Williams Company

DISTNAME =		z80as-2.0
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/udo-munk/z80as

GH_ACCOUNT =		udo-munk
GH_PROJECT =		z80as
GH_COMMIT =		5f0507502b8026c75ab8150ee55488663a941353

WANTLIB +=		c

NO_TEST =		Yes

do-build:
			cd ${WRKBUILD} && ${MAKE}

post-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/z80as/examples
		cp -R ${WRKSRC}/basic.* ${PREFIX}/share/z80as/examples

.include <bsd.port.mk>
