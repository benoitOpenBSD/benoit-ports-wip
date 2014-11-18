# $OpenBSD$

COMMENT =		Open-source Ultima 7 engine

DISTNAME =		exult-1.2
CATEGORIES =		games

HOMEPAGE =		http://exult.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		SDL c m stdc++ pthread z vorbisfile xcb vorbis
WANTLIB +=		X11 Xau Xdmcp Xext Xrandr Xrender Xxf86dga Xxf86vm
WANTLIB +=		iconv mikmod ogg pthread-stubs smpeg sndio usbhid
WANTLIB +=		SDL_mixer
                        
MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=exult/}

RUN_DEPENDS =		devel/desktop-file-utils
LIB_DEPENDS =		devel/sdl-mixer

USE_GROFF =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
#CONFIGURE_ARGS +=	${CONFIGURE_SHARED}
CONFIGURE_ENV =         CXXFLAGS="-O0"

NO_TEST =		Yes

.include <bsd.port.mk>
