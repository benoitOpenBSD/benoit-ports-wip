# $OpenBSD$

COMMENT =		BASIC interpreter/compiler for UNIX

DISTNAME =		X11Basic-1.27
PKGNAME =		${DISTNAME:L}
CATEGORIES =		lang

HOMEPAGE =		http://x11-basic.sourceforge.net/

# GPLv2
PERMIT_PACKAGE		= Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

GH_ACCOUNT =            kollokollo
GH_PROJECT =            X11Basic
GH_COMMIT =             82479decdb06f8ab70d5d834816baba1d0ad9d30

LIB_DEPENDS =		devel/sdl devel/gmp

WANTLIB =		c

SDL_CONFIG =		${LOCALBASE}/bin/sdl-config

USE_GMAKE =		Yes

WRKSRC =		${WRKDIST}/src

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="`${SDL_CONFIG} --cflags` \
			-I${X11BASE}/include \
			-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
CONFIGURE_ARGS =	${CONFIGURE_SHARED} \
			--with-sdl \
			--enable-cryptography \
			--without-bluetooth \
			--without-usb 

.include <bsd.port.mk>
