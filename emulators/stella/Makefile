# $OpenBSD: Makefile,v 1.23 2013/07/04 12:44:29 benoit Exp $

COMMENT =		Atari 2600 VCS emulator

V =			5.0.2
DISTNAME =		stella-${V}
CATEGORIES =		emulators
DISTFILES =		stella-${V}-src.tar.xz

HOMEPAGE =		https://stella-emu.github.io/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c ${COMPILER_LIBCXX} m z pthread SDL2 png

MASTER_SITES =		https://github.com/${GH_ACCOUNT}/${GH_PROJECT}/releases/download/${GH_TAGNAME}/
GH_ACCOUNT =            stella-emu
GH_PROJECT =            stella
GH_TAGNAME =            $V

EXTRACT_SUFX =		.tar.xz

LIB_DEPENDS =		devel/sdl2 \
			graphics/png

# c++11
#MODULES +=		gcc4
#MODGCC4_ARCHS =		*
#MODGCC4_LANGS =		c c++

CXXFLAGS +=		-I${X11BASE}/include -I${LOCALBASE}/include
LDFLAGS +=		-L${LOCALBASE}/lib

CONFIGURE_STYLE =	simple
CONFIGURE_ARGS +=	--disable-gl --with-libpng-prefix=${LOCALBASE}

USE_GMAKE =		Yes

NO_TEST =		Yes

DOCSBASE =		${WRKDIST}/docs
HTMLDOCS =		${DOCSBASE}/*.html
HTMLGRAPHICS =		${DOCSBASE}/graphics/*.png
DOCSDIR =		${PREFIX}/share/doc/stella

do-install:
	${INSTALL_PROGRAM}	${WRKDIST}/stella ${PREFIX}/bin

post-install:
	${INSTALL_DATA_DIR} ${DOCSDIR}
	${INSTALL_DATA} ${HTMLDOCS} ${DOCSDIR}
	${INSTALL_DATA_DIR} ${DOCSDIR}/graphics
	${INSTALL_DATA} ${HTMLGRAPHICS} ${DOCSDIR}/graphics/

.include <bsd.port.mk>
