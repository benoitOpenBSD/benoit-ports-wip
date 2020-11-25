# $OpenBSD$

COMMENT =		Apple ][ emulator

DISTNAME =		linapple-pie-20181023
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/dabonetn/linapple-pie

GH_ACCOUNT =		dabonetn
GH_PROJECT =		linapple-pie
GH_COMMIT =		c22ba0c3ad6c317b4f13486b7ff06a340c831122

WANTLIB +=		c m z c++ c++abi pthread curl zip \
			SDL SDL_image

LIB_DEPENDS =		net/curl \
			archivers/libzip \
			devel/sdl \
			devel/sdl-image

USE_GMAKE =		Yes

DEBUG_PACKAGES =	${BUILD_PACKAGES}

do-build:
			cd ${WRKSRC}/src && ${MAKE_PROGRAM}

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/linapple ${PREFIX}/bin/
		${INSTALL_DATA_DIR} ${PREFIX}/linapple
		cp ${WRKSRC}/linapple.conf ${PREFIX}/linapple
		cp ${WRKSRC}/Master.dsk ${PREFIX}/linapple
		${INSTALL_DATA_DIR} ${PREFIX}/linapple/images
		${INSTALL_DATA_DIR} ${PREFIX}/linapple/ftp/cache

.include <bsd.port.mk>
