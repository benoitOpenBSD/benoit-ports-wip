# $OpenBSD$

COMMENT =		assembler for MSP430, dsPIC and others

DISTNAME =		naken-asm-20200518
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		https://github.com/mikeakohn/naken_asm

GH_ACCOUNT =		mikeakohn
GH_PROJECT =		naken_asm
GH_COMMIT =		db759a98943a7b1282777056ba0c4eb9a4de0a0e

WANTLIB +=		c curses readline

MODULES =		lang/python

CONFIGURE_STYLE =	simple
CONFIGURE_ARGS =	--enable-all

BUILD_DEPENDS =		shells/bash

USE_GMAKE =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/naken_asm ${PREFIX}/bin
			${INSTALL_PROGRAM} ${WRKSRC}/naken_util ${PREFIX}/bin

do-test:
			@cd ${WRKSRC} && exec ${SETENV} ${MAKE_ENV} \
			${MAKE_PROGRAM} tests

.include <bsd.port.mk>
