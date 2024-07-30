COMMENT =		ngspice shared library, based on Berkeley SPICE

PKGNAME =		libngspice-${V}

SHARED_LIBS +=		ngspice			1.0 # 0.0

WANTLIB += 		${COMPILER_LIBCXX} m pthread fftw3

LIB_DEPENDS +=		math/fftw3 \
			devel/readline

#BUILD_DEPENDS =		devel/libtool

CONFIGURE_ARGS =        --with-fftw3=yes --enable-cider --with-ngshared

CONFIGURE_ENV =         LDFLAGS="${LDFLAGS} -L${X11BASE}/lib -L${PREFIX}/lib -L${LOCALBASE}/lib" \
                        CFLAGS="${CFLAGS} -I${LOCALBASE}/include -I${X11BASE}/include \
                        -I/usr/X11R6/include/freetype2" \
                        CXXFLAGS="${CXXFLAGS} -I${LOCALBASE}/include"

# same tests as cad/ngspice/ngspice, but they assume you've built a binary
NO_TEST =		Yes

post-install:
	@rm -r ${PREFIX}/share/ngspice/

.include <bsd.port.mk>
