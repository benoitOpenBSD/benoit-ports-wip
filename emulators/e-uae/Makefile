# $OpenBSD$

COMMENT =	Enhanced UAE
DISTNAME =	e-uae-0.8.29-WIP4
CATEGORIES =	emulators

HOMEPAGE =	http://www.rcdrummond.net/uae/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =	ICE SM X11 Xau Xcursor Xdmcp Xext Xfixes Xi Xinerama \
		Xcomposite Xdamage gio-2.0 \
		Xrandr Xrender Xxf86dga Xxf86vm atk-1.0 c cairo expat \
		fontconfig freetype glib-2.0 glitz gmodule-2.0 gobject-2.0 \
		m pango-1.0 pangocairo-1.0 pangoft2-1.0 pixman-1 png pthread z

MASTER_SITES =		http://www.rcdrummond.net/uae/e-uae-0.8.29-WIP4/ \
			http://www.arcane-labs.net/download/OpenBSD/

EXTRACT_SUFX =		.tar.bz2

MODULES =		devel/gettext

LIB_DEPENDS +=		gdk_pixbuf-2.0,gdk-x11-2.0,gtk-x11-2.0::x11/gtk+2
LIB_DEPENDS +=		SDL::devel/sdl

USE_GMAKE =		Yes
USE_X11 =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--with-x \
			--with-sdl-sound \
			--with-sdl --with-sdl-gfx \
			--with-caps --with-zlib \
			--with-gtk-prefix=${PREFIX}

NO_REGRESS =		Yes

# Workaround compiler bug on hppa: cc1plus spinning forever
.if ${MACHINE_ARCH} == "hppa"
CFLAGS+=	-O0
.endif

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
