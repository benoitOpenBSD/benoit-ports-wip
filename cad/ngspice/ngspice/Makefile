COMMENT =		circuit simulator, based on Berkeley SPICE

WANTLIB += 		${COMPILER_LIBCXX} ICE SM X11 Xau Xaw Xdmcp Xext Xmu
WANTLIB +=		Xpm Xt Xft freetype c m xcb fftw3 ehistory ereadline

LIB_DEPENDS +=		math/fftw3 \
			devel/readline

BUILD_DEPENDS =		devel/libtool

RUN_DEPENDS =		math/gnuplot

CONFIGURE_ARGS =	--with-fftw3=yes --enable-cider --with-readline=yes  \
			--enable-klu --enable-sense2 --enable-predictor
#			--enable-osdi --enable-oldapps

CONFIGURE_ENV =		LDFLAGS="${LDFLAGS} -Lc++ -L${X11BASE}/lib -L${PREFIX}/lib -L${LOCALBASE}/lib" \
			CFLAGS="${CFLAGS} -I${LOCALBASE}/include -I${X11BASE}/include \
			-I${LOCALBASE}/include/ereadline -I/usr/X11R6/include/freetype2" \
			CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include"

FLAVORS =		xspice
FLAVOR ?=

.if ${FLAVOR:Mxspice}
CONFIGURE_ARGS +=	--with-x --enable-xspice
WANTLIB += 		pthread
.endif

post-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/ngspice/examples
			${INSTALL_DATA_DIR} ${PREFIX}/share/ngspice/tests
			cp -r ${WRKSRC}/examples/* \
				${PREFIX}/share/ngspice/examples/
			cp -r ${WRKSRC}/tests/* \
				${PREFIX}/share/ngspice/tests/
.include <bsd.port.mk>
