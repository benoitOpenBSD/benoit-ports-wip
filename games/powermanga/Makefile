# $OpenBSD$

COMMENT =		Arcade 2D shoot-em-up game

DISTNAME =		powermanga-0.90
CATEGORIES =		games

HOMEPAGE =		http://linux.tlk.fr/games/Powermanga/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		SDL c m pthread Xext Xxf86dga SDL_mixer

MASTER_SITES =		http://linux.tlk.fr/games/Powermanga/download/

LIB_DEPENDS =		devel/sdl-mixer

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu

NO_REGRESS =		Yes

pre-configure:
			${SUBST_CMD} ${WRKSRC}/powermanga.6
		
.include <bsd.port.mk>
