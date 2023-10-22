
COMMENT =		hammer of Thyrion

V = 			1.4.3
DISTNAME =		hexen2source-${V}
PKGNAME =		hexen2-${V}

CATEGORIES =		games

HOMEPAGE =		http://uhexen2.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c SDL m pthread SDL_mixer

SITES =			${SITE_SOURCEFORGE:=uhexen2/}

EXTRACT_SUFX =		.tgz

LIB_DEPENDS =		devel/sdl-mixer

USE_GROFF =		Yes
USE_GMAKE =		Yes

NO_TEST =		Yes

WRKSRC =		${WRKDIST}/hexen2

ALL_TARGET =		glh2

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/glhexen2 ${PREFIX}/bin/

.include <bsd.port.mk>
