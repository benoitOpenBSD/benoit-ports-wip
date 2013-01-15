# $OpenBSD$

COMMENT =	top-down terminal for Gnome

DISTNAME =	guake-0.4.4
CATEGORIES =	x11

HOMEPAGE =	http://guake.org/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB += GL X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes
WANTLIB += Xi Xinerama Xrandr Xrender Xxf86vm atk-1.0 cairo drm
WANTLIB += expat ffi fontconfig freetype gdk-x11-2.0 gdk_pixbuf-2.0
WANTLIB += gio-2.0 glib-2.0 gmodule-2.0 gobject-2.0 gthread-2.0
WANTLIB += gtk-x11-2.0 harfbuzz icudata icule icuuc m pango-1.0
WANTLIB += pangocairo-1.0 pangoft2-1.0 pcre pixman-1 png pthread
WANTLIB += pthread-stubs python2.7 stdc++ xcb xcb-render xcb-shm z

MASTER_SITES =	${HOMEPAGE}files/

MODULES =	devel/gettext \
		textproc/intltool \
		lang/python \
		devel/gconf2

BUILD_DEPENDS =	devel/gconf2 \
		devel/vte,-python \
		x11/py-gtk2 \
		x11/gtk+2
		
RUN_DEPENDS =	devel/py-notify \
		devel/vte,-python \
		devel/gconf2 \
		x11/py-gtk2 \
		devel/gsettings-desktop-schemas
				 
USE_GMAKE =	Yes
USE_LIBTOOL =	Yes

MODGNOME_DESKTOP_FILE =	Yes
MODGNOME_ICON_CACHE =	Yes

CONFIGURE_STYLE = gnu
CONFIGURE_ARGS = ${CONFIGURE_SHARED} \
		--with-gconf-schema-file-dir=${LOCALBASE}/share/schemas/guake
CONFIGURE_ENV =	CPPFLAGS="-I${LOCALBASE}/include -I${X11BASE}/include" \
		LDFLAGS="-L${LOCALBASE}/lib" \
		GCONF_SCHEMA_FILE_DIR="${PREFIX}/share/schemas/guake"
	
.include <bsd.port.mk>
