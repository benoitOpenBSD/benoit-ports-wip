COMMENT =	reimplementation of the PICO-8 fantasy console

DIST_TUPLE +=	github benbaker76 femto8 v1.0.00 .

CATEGORIES =	games
MAINTAINER =	Thomas Frohwein <thfr@openbsd.org>

# MIT
PERMIT_PACKAGE = Yes

WANTLIB += ${COMPILER_LIBCXX} SDL c m

# uses some C++ like namespace, templates
COMPILER =	base-clang ports-gcc base-gcc

LIB_DEPENDS =	devel/sdl

USE_GMAKE =	Yes

DEBUG_PACKAGES = ${BUILD_PACKAGES}

NO_TEST =	Yes

# no install target
do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/build-linux/femto8 ${PREFIX}/bin/

.include <bsd.port.mk>
