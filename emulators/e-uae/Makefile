# $OpenBSD$

COMMENT =	Enhanced UAE
DISTNAME =	e-uae-0.8.29-WIP4
CATEGORIES =	emulators

HOMEPAGE =	http://www.rcdrummond.net/uae/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB +=	SDL X11 Xcomposite Xcursor Xdamage Xext Xfixes Xi Xinerama
WANTLIB +=	Xrandr Xrender c fontconfig freetype m pthread z glib-2.0
WANTLIB +=	pango-1.0 pangocairo-1.0 pangoft2-1.0 atk-1.0 cairo harfbuzz
WANTLIB +=	intl gtk-x11-2.0 gobject-2.0 gio-2.0 gdk_pixbuf-2.0 gdk-x11-2.0

MASTER_SITES =		http://www.rcdrummond.net/uae/e-uae-0.8.29-WIP4/ \
			https://www.arcane-labs.net/download/OpenBSD/

EXTRACT_SUFX =		.tar.bz2

LIB_DEPENDS +=		devel/gettext,-runtime \
			x11/gtk+2 \
			devel/sdl

USE_GMAKE =		Yes
USE_X11 =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--with-x \
			--with-sdl-sound \
			--with-sdl --with-sdl-gfx \
			--with-caps --with-zlib \
			--with-gtk-prefix=${PREFIX}

NO_TEST =		Yes

DOCS=		COMPATIBILITY CREDITS FAQ NEWS README README.PROGRAMMERS

FILES=		mousehack timehack transdisk transrom uae-control \
		uae-control.info uae_rcli uaectrl

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/src/uae ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/src/readdisk ${PREFIX}/bin
	${INSTALL_DATA_DIR} ${PREFIX}/share/uae/amiga/source
	${INSTALL_DATA} ${WRKSRC}/docs/*.txt ${PREFIX}/share/uae
	${INSTALL_DATA} ${WRKSRC}/amiga/source/* ${PREFIX}/share/uae/amiga/source

.include <bsd.port.mk>
