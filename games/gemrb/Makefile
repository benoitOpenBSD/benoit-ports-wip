
COMMENT =		portable open-source implementation of BIE

DISTNAME =		gemrb-0.6.3
#PKGNAME =		${DISTNAME:L}
CATEGORIES =		games

HOMEPAGE =		http://gemrb.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		SDL c m png pthread z GL stdc++ SDL_image SDL_mixer \
			openal

SITES =			${SITE_SOURCEFORGE:=gemrb/}

MODULES =		devel/cmake lang/python devel/gettext

LIB_DEPENDS =		devel/sdl-image \
			devel/sdl-mixer \
			audio/openal \
			graphics/png

#USE_GROFF =		Yes
USE_GMAKE =		Yes
#USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	cmake
CONFIGURE_ARGS =	-DDISABLE_WERROR=1
#CONFIGURE_ENV =		CPPFLAGS="-I${X11BASE}/include -I${LOCALBASE}/include \
#			-I${LOCALBASE}/include/libpng" \
#			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

.include <bsd.port.mk>
