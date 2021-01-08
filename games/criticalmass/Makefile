# $OpenBSD$

COMMENT =		Space shootemup resembling Galaxian

DISTNAME =		CriticalMass-1.5
PKGNAME =		${DISTNAME:L}
CATEGORIES =		games

HOMEPAGE =		http://criticalmass.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =		SDL c m png pthread z GL stdc++ SDL_image SDL_mixer

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=criticalmass/}

EXTRACT_SUFX =		.tar.bz2

LIB_DEPENDS =		devel/sdl-image \
			devel/sdl-mixer \
			graphics/png \
			net/curl

USE_GROFF =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${X11BASE}/include -I${LOCALBASE}/include \
			-I${LOCALBASE}/include/libpng" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

.include <bsd.port.mk>
