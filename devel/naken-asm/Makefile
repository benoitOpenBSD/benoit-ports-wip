# $OpenBSD$

COMMENT =		assembler for MSP430, dsPIC and others

DISTNAME =		naken-asm-20200421
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/mikeakohn/naken_asm

GH_ACCOUNT =		mikeakohn
GH_PROJECT =		naken_asm
GH_COMMIT =		adcc1a8f52b977166c5abd175945bbacb3bd4fec

WANTLIB +=		c curses readline

CONFIGURE_STYLE =	simple
CONFIGURE_ARGS =	--enable-all

BUILD_DEPENDS =		shells/bash

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/naken_asm ${PREFIX}/bin
			${INSTALL_PROGRAM} ${WRKSRC}/naken_util ${PREFIX}/bin

.include <bsd.port.mk>
