# $OpenBSD$

COMMENT =		classical memory game

DISTNAME =		lpairs-1.0.4
CATEGORIES =		games

HOMEPAGE =		http://lgames.sourceforge.net/index.php?project=LPairs

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		SDL c pthread SDL

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=lgames/}

MODULES =		devel/gettext
LIB_DEPENDS =		devel/sdl

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV +=	LDFLAGS="-L${LOCALBASE}/lib" \
			LIBS="-liconv -lintl"

NO_REGRESS =		Yes

.include <bsd.port.mk>
