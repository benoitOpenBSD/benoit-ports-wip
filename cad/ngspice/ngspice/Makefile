COMMENT =		circuit simulator, based on Berkeley SPICE

WANTLIB += 		${COMPILER_LIBCXX} ICE SM X11 Xau Xaw Xdmcp Xext Xmu
WANTLIB +=		Xpm Xt Xft freetype c m xcb fftw3 ehistory ereadline

LIB_DEPENDS +=		math/fftw3 \
			devel/readline

BUILD_DEPENDS =		devel/libtool

CONFIGURE_ARGS =	--with-fftw3=yes --enable-cider --with-readline=yes

CONFIGURE_ENV =		LDFLAGS="${LDFLAGS} -Lc++ -L${X11BASE}/lib -L${PREFIX}/lib -L${LOCALBASE}/lib" \
			CFLAGS="${CFLAGS} -I${LOCALBASE}/include -I${X11BASE}/include \
			-I${LOCALBASE}/include/ereadline -I/usr/X11R6/include/freetype2" \
			CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include"

.include <bsd.port.mk>
