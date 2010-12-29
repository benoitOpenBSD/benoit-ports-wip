# $OpenBSD: Makefile,v 1.16 2009/03/14 16:49:18 ajacoutot Exp $

COMMENT=	UAE amiga emulator
DISTNAME=	uae-0.8.29
CATEGORIES=	emulators x11

HOMEPAGE=	http://www.amigaemulator.org/

# GPLv2
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=	ICE SM X11 Xau Xcursor Xdmcp Xext Xfixes Xi Xinerama \
		Xcomposite Xdamage gio-2.0 \
		Xrandr Xrender Xxf86dga Xxf86vm atk-1.0 c cairo expat \
		fontconfig freetype glib-2.0 glitz gmodule-2.0 gobject-2.0 \
		m pango-1.0 pangocairo-1.0 pangoft2-1.0 pixman-1 png pthread z

MASTER_SITES=	ftp://ftp.amigaemulator.org/pub/uae/sources/develop/ \
		http://www.arcane-labs.net/download/OpenBSD/

EXTRACT_SUFX =	.tar.bz2

MODULES=	devel/gettext
LIB_DEPENDS+=	gdk_pixbuf-2.0,gdk-x11-2.0,gtk-x11-2.0::x11/gtk+2

USE_X11=		Yes
CONFIGURE_STYLE=	gnu
CONFIGURE_ARGS+=	--enable-dga --enable-vidmode --without-oss-sound

FLAVORS=	sdl
FLAVOR?=

.if ${FLAVOR:L:Msdl}
CONFIGURE_ARGS+=	--with-sdl-sound --with-sdl --with-sdl-gfx
LIB_DEPENDS+=		SDL::devel/sdl
.endif

NO_REGRESS=	Yes

# Workaround compiler bug on hppa: cc1plus spinning forever
.if ${MACHINE_ARCH} == "hppa"
CFLAGS+=	-O0
.endif

DOCS=		COMPATIBILITY CREDITS FAQ NEWS README README.PROGRAMMERS

FILES=		mousehack timehack transdisk transrom uae-control \
		uae-control.info uae_rcli uaectrl

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/uae ${PREFIX}/bin
	${INSTALL_PROGRAM} ${WRKSRC}/readdisk ${PREFIX}/bin
	${INSTALL_DATA_DIR} ${PREFIX}/share/uae/amiga
	cd ${WRKSRC}/docs && ( \
	  ${INSTALL_DATA} ${DOCS} ${PREFIX}/share/uae; \
	  ${INSTALL_DATA} unix/README ${PREFIX}/share/uae/README.unix )
	cd ${WRKSRC}/amiga && ${INSTALL_DATA} ${FILES} \
	  ${PREFIX}/share/uae/amiga

.include <bsd.port.mk>
