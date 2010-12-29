# $OpenBSD$

COMMENT =		hacked Hexen

DISTNAME =		hhexen-1.6.1-src
PKGNAME =		${DISTNAME:S/-src//}
CATEGORIES =		games

HOMEPAGE =		http://hhexen.sourceforge.net/hhexen.html

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		c GL GLU m pthread SDL

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=hhexen/}

EXTRACT_SUFX =		.tgz

LIB_DEPENDS +=		devel/sdl

USE_GROFF =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--with-datapath="${PREFIX}/share/hhexen" \
			--enable-assassin
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_REGRESS =		Yes

ALL_TARGET =		opengl

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/hhexen
	cp ${WRKSRC}/assassin.wad ${PREFIX}/share/hhexen
	${INSTALL_PROGRAM} ${WRKSRC}/hhexen-gl ${PREFIX}/bin/

.include <bsd.port.mk>
