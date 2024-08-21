COMMENT =	circuit simulator, based on Berkeley SPICE

WANTLIB += ${COMPILER_LIBCXX} ICE SM X11 Xau Xaw Xdmcp Xext Xft
WANTLIB += Xmu Xpm Xrender Xt c curses expat fontconfig freetype
WANTLIB += m readline xcb z

CONFIGURE_ARGS +=	--with-x \
			--enable-klu --enable-sense2 --enable-predictor \
			--enable-osdi

RUN_DEPENDS =		cad/gtkwave \
			math/gnuplot

post-install:
			${INSTALL_DATA_DIR} ${PREFIX}/share/ngspice/examples
			${INSTALL_DATA_DIR} ${PREFIX}/share/ngspice/tests
			cp -r ${WRKSRC}/examples/* \
				${PREFIX}/share/ngspice/examples/
			cp -r ${WRKSRC}/tests/* \
				${PREFIX}/share/ngspice/tests/

.include <bsd.port.mk>
