
COMMENT =		assembler for MSP430, dsPIC and others

DISTNAME =		naken-asm-20260531
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/mikeakohn/naken_asm

GH_ACCOUNT =		mikeakohn
GH_PROJECT =		naken_asm
GH_COMMIT =		247c23706909f09bac77c587780b8a826bbda27c

WANTLIB +=		c curses readline

MODULES =		lang/python

CONFIGURE_STYLE =	simple
CONFIGURE_ARGS =	--enable-all

BUILD_DEPENDS =		shells/bash

MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

USE_GMAKE =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/naken_asm ${PREFIX}/bin
			${INSTALL_PROGRAM} ${WRKSRC}/naken_util ${PREFIX}/bin

do-test:
			@cd ${WRKSRC} && exec ${SETENV} ${MAKE_ENV} \
			${MAKE_PROGRAM} tests

.include <bsd.port.mk>
