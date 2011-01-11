# $OpenBSD$

COMMENT =		free implementation of Heroes of the Might and Magic II engine

DISTNAME =		fheroes2-src-r2187
PKGNAME =		${DISTNAME:S/-src//}
CATEGORIES =		games

HOMEPAGE =		http://sourceforge.net/projects/fheroes2/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2+
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		SDL c m png pthread z GL stdc++ SDL_image SDL_mixer \
			SDL_net SDL_ttf

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=fheroes2/}

EXTRACT_SUFX =		.tgz

MODULES =		devel/gettext

LIB_DEPENDS =		devel/sdl-image \
			devel/sdl-mixer \
			devel/sdl-net \
			devel/sdl-ttf \
			graphics/png

USE_GROFF =		Yes
USE_GMAKE =		Yes

WRKDIST =               ${WRKDIR}/fheroes-src

NO_REGRESS =		Yes

.include <bsd.port.mk>
