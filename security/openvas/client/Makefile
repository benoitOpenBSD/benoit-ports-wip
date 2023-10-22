
COMMENT =		OpenVAS security scanner client
DISTNAME =		openvas-client-2.0.5

SITES =			${SITES_OPENVAS:=570/}

WANTLIB +=		X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes
WANTLIB +=		Xi Xinerama Xrandr Xrender atk-1.0 c cairo crypto expat
WANTLIB +=		fontconfig freetype gio-2.0 glib-2.0 glitz gmodule-2.0
WANTLIB +=		gobject-2.0 m pango-1.0 pangocairo-1.0 pangoft2-1.0
WANTLIB +=		pthread-stubs xcb pixman-1 png ssl z

LIB_DEPENDS +=		gdk-x11-2.0,gdk_pixbuf-2.0,gtk-x11-2.0::x11/gtk+2

MODULES =		devel/gettext

USE_X11 =		Yes
USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--enable-gtk

.include <bsd.port.mk>
