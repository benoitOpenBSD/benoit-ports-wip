
COMMENT =		3D game inspired by the movie Tron

DISTNAME =		gltron-0.70
CATEGORIES =		games

HOMEPAGE =		http://gltron.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2+
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		SDL c z GL m mikmod ogg pthread smpeg
WANTLIB +=		stdc++ vorbis vorbisfile SDL_sound png

SITES =			${SITE_SOURCEFORGE:=gltron/}

LIB_DEPENDS =		devel/sdl-sound \
			graphics/png

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${X11BASE}/include -I${LOCALBASE}/include/libpng" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

.include <bsd.port.mk>
