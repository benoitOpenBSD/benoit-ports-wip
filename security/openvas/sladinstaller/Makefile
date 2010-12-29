# $OpenBSD$

COMMENT =		sladinstaller for OpenVAS
V =			1.1.2
DISTNAME =		sladinstaller-${V}
PKGNAME =		openvas-slad-${V}

MASTER_SITES =		${MASTER_SITES_OPENVAS:=516/}

WANTLIB +=		X11 Xau Xcomposite Xcursor Xdamage Xdmcp Xext Xfixes
WANTLIB +=		Xi Xinerama Xrandr Xrender atk-1.0 c cairo crypto expat
WANTLIB +=		fontconfig freetype glib-2.0 glitz gmodule-2.0 gobject-2.0
WANTLIB +=		gthread-2.0 idn m pango-1.0 pangocairo-1.0 pangoft2-1.0
WANTLIB +=		pthread-stubs xcb pixman-1 png pthread ssl stdc++ z

LIB_DEPENDS =		curl::net/curl \
			gdk-x11-2.0,gdk_pixbuf-2.0,gtk-x11-2.0::x11/gtk+2

MODULES =		devel/gettext

USE_X11 =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		No

.include <bsd.port.mk>
