COMMENT =	interpreter for the programming language APL
DISTNAME =	apl-1.9
CATEGORIES =	lang

SHARED_LIBS +=	_sql                      0.0 # 0.0
SHARED_LIBS +=	emacs                     1.0 # 1.0

HOMEPAGE =	https://www.gnu.org/software/apl/
MAINTAINER =	Brian Callahan <bcallah@openbsd.org>

# GPLv3+
PERMIT_PACKAGE =	Yes

WANTLIB += ${COMPILER_LIBCXX} X11 Xau Xcomposite Xcursor Xdamage
WANTLIB += Xdmcp Xext Xfixes Xi Xinerama Xrandr Xrender atk-1.0
WANTLIB += atk-bridge-2.0 atspi c cairo cairo-gobject curses dbus-1
WANTLIB += epoll-shim epoxy execinfo expat ffi fftw3 fontconfig
WANTLIB += freetype fribidi gdk-3 gdk_pixbuf-2.0 gio-2.0 glib-2.0
WANTLIB += gmodule-2.0 gobject-2.0 graphite2 gtk-3 harfbuzz iconv
WANTLIB += intl jpeg m pango-1.0 pangocairo-1.0 pangoft2-1.0 pcre2-32
WANTLIB += pcre2-8 pixman-1 png wayland-client wayland-cursor
WANTLIB += wayland-egl xcb xcb-render xcb-shm xkbcommon z

DEBUG_PACKAGES =	${BUILD_PACKAGES}

COMPILER =	base-clang ports-gcc
CXXFLAGS_base-clang =	-std=c++14

SITES =		${SITE_GNU:=apl/}

LIB_DEPENDS =	devel/pcre2 \
		math/fftw3 \
		x11/gtk+3

RUN_DEPENDS =	fonts/apl-fonts

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--without-sqlite3 \
			--without-postgresql
CONFIGURE_ENV +=	CXX_WERROR=no \
			CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include" \
			LDFLAGS="${LDFLAGS} -L${LOCALBASE}/lib"

USE_GMAKE =	Yes

FAKE_FLAGS =	sysconfdir=${PREFIX}/share/examples/apl

pre-configure:
	sed -i 's,-O2,,g' ${WRKSRC}/configure \
		${WRKSRC}/src/{APs,native}/Makefile.in

.include <bsd.port.mk>
