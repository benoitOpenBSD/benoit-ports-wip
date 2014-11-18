# $OpenBSD$

COMMENT =		janusz Pelcs Robbo for the Atari XE/XL

DISTNAME =		gnurobbo-0.65-source
PKGNAME =		${DISTNAME:S/-source//}
CATEGORIES =		games

HOMEPAGE =		http://gnurobbo.sourceforge.net

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		SDL c m pthread SDL_mixer SDL_image SDL_ttf

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=gnurobbo/}

LIB_DEPENDS =		devel/sdl-mixer \
			devel/sdl-image \
			devel/sdl-ttf

USE_GROFF =		Yes
USE_GMAKE =		Yes

NO_TEST =		Yes

WRKDIST =		${WRKDIR}/${PKGNAME}
WRKSRC =		${WRKDIST}

pre-configure:
		${SUBST_CMD} ${WRKSRC}/Makefile

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/gnurobbo ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/gnurobbo
		(cd ${WRKSRC}/data && tar -cf - * ) | \
			(cd ${PREFIX}/share/gnurobbo && tar -xf - )
		chown -R ${SHAREOWN}:games ${PREFIX}/share/gnurobbo

.include <bsd.port.mk>
