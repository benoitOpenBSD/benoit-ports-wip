# $OpenBSD$

COMMENT =		Dstroy is a bomberman-like.

DISTNAME =		dstroy-1.7
#DISTNAME =		dstroySrc_20090214
#PKGNAME =		dstroy-1.7
CATEGORIES =		games

HOMEPAGE =		http://narroin.free.fr/dstroy/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		c m pthread stdc++ SDL SDL_image SDL_mixer
WANTLIB +=		mikmod ogg smpeg vorbis vorbisfile SDL_net

MASTER_SITES =		https://www.arcane-labs.com/download/OpenBSD/
#MASTER_SITES =		http://narroin.free.fr/dstroy/res/
#MASTER_SITES0 =	http://narroin.free.fr/dstroy/res/
#DISTFILES =		dstroySrc_20090214.zip DstroyDS_20090130.rar:0
#EXTRACT_SUFX =		.zip
#EXTRACT_SUFX =		.rar

LIB_DEPENDS =		devel/sdl-image \
			devel/sdl-mixer \
			devel/sdl-net

MAKE_ENV =		CXX="${CXX}" CPPFLAGS="${CXXFLAGS} \
			-I${PREFIX}/include -I${X11BASE}/include" \

USE_GROFF =		Yes
USE_GMAKE =		Yes

NO_TEST =		Yes

MAKE_FILE =		Makefile.linux
#WRKSRC =		${WRKDIR}/dstroy_src

pre-configure:
		${SUBST_CMD} ${WRKSRC}/src/DstroyGlobals.h ${WRKSRC}/src/TGIGlobals.cpp
		
do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/dstroy ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/dstroy
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/dstroy
		${INSTALL_DATA} ${WRKSRC}/LICENSE* ${PREFIX}/share/doc/dstroy
		(cd ${WRKSRC}/dstroydata && tar -cf - * ) | \
			(cd ${PREFIX}/share/dstroy && tar -xf - )
		chown -R ${SHAREOWN}:games ${PREFIX}/share/dstroy
		
.include <bsd.port.mk>
