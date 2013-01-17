# $OpenBSD$

COMMENT =		Atomix clone

DISTNAME =		lmarbles-1.0.8
CATEGORIES =		games

HOMEPAGE =		http://lgames.sourceforge.net/index.php?project=LMarbles

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		SDL c m pthread SDL_mixer

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=lgames/}

RUN_DEPENDS =		devel/desktop-file-utils
LIB_DEPENDS =		devel/sdl-mixer

USE_GMAKE =		Yes

LOCALSTATEDIR=  ${BASELOCALSTATEDIR}/games

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--enable-ascii
NO_REGRESS =		Yes

post-install:
		${INSTALL_DATA} ${WRKSRC}/src/empty.prfs /var/games/
		
.include <bsd.port.mk>
