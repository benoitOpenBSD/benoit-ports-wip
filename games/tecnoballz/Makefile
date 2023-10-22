
COMMENT =		A exciting Brick Breaker

DISTNAME =		tecnoballz-0.92
CATEGORIES =		games

HOMEPAGE =		http://linux.tlk.fr/games/TecnoballZ/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		SDL c m pthread ogg stdc++ mikmod smpeg SDL_image SDL_mixer
WANTLIB +=		vorbis vorbisfile

SITES =			http://linux.tlk.fr/games/TecnoballZ/download/

EXTRACT_SUFX =		.tgz

LIB_DEPENDS =		devel/sdl-image \
			devel/sdl-mixer \
			audio/libvorbis

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		LDFLAGS="-L${LOCALBASE}/lib" \
			CPPFLAGS="${CXXFLAGS} -I${LOCALBASE}/include -I${LOCALBASE}/include/vorbis"

NO_TEST =		Yes

post-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/tecnoballz/texts
			${INSTALL_DATA} ${WRKSRC}/src/TecnoballZ/texts/* \
				 ${PREFIX}/share/tecnoballz/texts
			${INSTALL_DATA} ${WRKSRC}/tecnoballz.hi /var/games/tecnoballz

.include <bsd.port.mk>
