
COMMENT =		a classic player for a modern era

DISTNAME =		eina-0.8.0

SHARED_LIBS +=		gel-1.0		0.0	# .1.0
SHARED_LIBS +=		lomo-1.0	0.0	# .1.0

CATEGORIES =		audio

HOMEPAGE =		http://eina.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes
WANTLIB +=		Xi Xinerama Xrandr Xrender c crypto expat fontconfig
WANTLIB +=		freetype m pixman-1 pthread pthread-stubs ssl xcb z idn
WANTLIB +=		atk-1.0 cairo gio-2.0 glib-2.0 glitz gmodule-2.0 gobject-2.0
WANTLIB +=		gthread-2.0 pango-1.0 pangocairo-1.0 pangoft2-1.0 pcre
WANTLIB +=		dbus-1 dbus-glib-1 gstreamer-0.10

SITES =			${SITE_SOURCEFORGE:=eina/}

MODULES =		devel/gettext

LIB_DEPENDS =		databases/sqlite3 \
			graphics/png \
			gdk-x11-2.0,gdk_pixbuf-2.0,gtk-x11-2.0::x11/gtk+2 \
			net/curl \
			textproc/libxml \
			devel/libnotify \
			devel/libunique \
			multimedia/gstreamer-0.10/plugins-base
			
USE_X11 =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include -I${X11BASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib -L${X11BASE}/lib"

NO_TEST =		Yes

.include <bsd.port.mk>
