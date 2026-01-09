COMMENT =	ngspice shared library, based on Berkeley SPICE

PKGNAME =	libngspice-${V}

SHARED_LIBS +=  ngspice                1.0 # 0.14

WANTLIB += ${COMPILER_LIBCXX} m pthread

CONFIGURE_ARGS +=	--with-ngshared \
			--enable-shared

# same tests as cad/ngspice/ngspice, but they assume you've built a binary
NO_TEST =	Yes

post-install:
	@rm -r ${PREFIX}/{lib,share}/ngspice/

.include <bsd.port.mk>
