# $OpenBSD$

COMMENT =		Arcade 2D shoot-em-up game

DISTNAME =		powermanga-0.91
CATEGORIES =		games

HOMEPAGE =		http://linux.tlk.fr/games/Powermanga/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		SDL c m pthread Xext Xxf86dga SDL_mixer

MASTER_SITES =		http://linux.tlk.fr/games/Powermanga/download/

LIB_DEPENDS =		devel/sdl-mixer \
			graphics/png

USE_GMAKE =		Yes

AUTOCONF_VERSION =	2.68
AUTOMAKE_VERSION=	1.11

CONFIGURE_STYLE= none
CONFIGURE_ENV=  	AUTOMAKE_VERSION="${AUTOMAKE_VERSION}" AUTOCONF_VERSION="${AUTOCONF_VERSION}" \
			CPPFLAGS="-I${LOCALBASE}/include -I${LOCALBASE}/include/libpng" \
                        LDFLAGS="-L${X11BASE}/lib -L${LOCALBASE}/lib"

NO_TEST =		Yes

do-configure:
			${SUBST_CMD} ${WRKSRC}/powermanga.6
			cd ${WRKSRC} && ${SETENV} ${CONFIGURE_ENV} /bin/sh ./bootstrap && \
			${SETENV} ${CONFIGURE_ENV} /bin/sh ./configure --enable-x11 \
			--disable-sdltest --disable-pngexport

.include <bsd.port.mk>
