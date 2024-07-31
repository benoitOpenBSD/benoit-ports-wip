
COMMENT =		amstrad CPC emulator

DISTNAME =		xcpc-0.50.0
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://www.xcpc-emulator.net

GH_ACCOUNT =		ponceto
GH_PROJECT =		xcpc-emulator
GH_COMMIT =		07838441f8df3f1ce0c863362a0f63ca6d2d3b8d

WANTLIB +=		c pthread
WANTLIB +=		atk-1.0 cairo cairo-gobject gdk-3 gdk_pixbuf-2.0 gio-2.0
WANTLIB +=		glib-2.0 gobject-2.0 gtk-3 harfbuzz intl pango-1.0
WANTLIB +=		pangocairo-1.0

LIB_DEPENDS =		x11/gtk+3

AUTOCONF_VERSION =	2.69
AUTOMAKE_VERSION =	1.16
CONFIGURE_STYLE =	autoreconf

CONFIGURE_ARGS =	--enable-gtk3 --enable-xshm CC="${CC}" CXX="${CXX}"

CONFIGURE_ENV =		CPPFLAGS="${CFLAGS} -I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
			
NO_TEST =		Yes

.include <bsd.port.mk>
