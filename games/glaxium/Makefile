
COMMENT =		A FREE OpenGL shoot them up

DISTNAME =		glaxium_0.5
PKGNAME =		${DISTNAME:S/_/-/}
CATEGORIES =		games

HOMEPAGE =		http://xhosxe.free.fr/glaxium/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		SDL c m pthread GL GLU z X11 Xi Xmu SDL_mixer png glut

SITES =			http://xhosxe.free.fr/glaxium/

LIB_DEPENDS =		devel/sdl-mixer \
			graphics/png \
			graphics/freeglut

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include -I${LOCALBASE}/include/libpng" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

ALL_TARGET =		glaxium

.include <bsd.port.mk>
