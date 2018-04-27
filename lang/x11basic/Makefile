# $OpenBSD$

COMMENT =	BASIC interpreter/compiler for UNIX

DISTNAME =	X11Basic-1.25
PKGNAME =	${DISTNAME:L}
CATEGORIES =	lang

HOMEPAGE=	http://x11-basic.sourceforge.net/

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=x11-basic/}

LIB_DEPENDS =		devel/sdl devel/gmp

WANTLIB =		c

SDL_CONFIG =		${LOCALBASE}/bin/sdl-config

USE_GMAKE =		Yes

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
