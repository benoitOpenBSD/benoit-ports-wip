# $OpenBSD: Makefile,v 1.14 2007/12/05 13:15:09 ajacoutot Exp $

COMMENT=	enhanced clone of Id Software's Doom game; multiplayer
DISTNAME=	prboom-2.5.0
CATEGORIES=	games x11
MASTER_SITES=	${MASTER_SITE_SOURCEFORGE:=prboom/}

HOMEPAGE=	http://prboom.sourceforge.net/

# GPL
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB=		SDL c m pthread GL GLU SDL_mixer>=3 SDL_net>=1 png>=4

USE_GROFF =	Yes

LIB_DEPENDS=	devel/sdl-mixer \
		devel/sdl-net \
		graphics/png

CONFIGURE_ENV+=	CPPFLAGS="-I${X11BASE}/include -I${LOCALBASE}/include/libpng" \
		LDFLAGS="-L${LOCALBASE}/lib"
CONFIGURE_STYLE=gnu
CONFIGURE_ARGS+=--disable-cpu-opt
MODGNU_CONFIG_GUESS_DIRS=${WRKSRC}/autotools

.include <bsd.port.mk>
