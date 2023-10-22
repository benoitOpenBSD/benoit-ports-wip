
COMMENT =		Hacked Heretic

DISTNAME =		hheretic-0.2.1-src
PKGNAME =		${DISTNAME:S/-src//}

CATEGORIES =		games

HOMEPAGE =		http://hhexen.sourceforge.net/hheretic.html

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c GL GLU m pthread SDL

SITES =			${SITE_SOURCEFORGE:=hhexen/}

EXTRACT_SUFX =		.tgz

LIB_DEPENDS +=		devel/sdl

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--with-datapath="${PREFIX}/share/hheretic"
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

ALL_TARGET =		opengl

do-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/hheretic
		${INSTALL_PROGRAM} ${WRKSRC}/hheretic-gl ${PREFIX}/bin/
		
.include <bsd.port.mk>
