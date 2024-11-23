
COMMENT =	the Vector Optimized Library

# git clone --recursive --branch v3.1.2 https://github.com/gnuradio/volk.git
DISTNAME =	volk-3.1.2
#GH_ACCOUNT =	gnuradio
#GH_PROJECT =	volk
#GH_TAGNAME =	v3.1.2

SHARED_LIBS +=  volk	1.0 # 3.1.2

CATEGORIES =	devel comms

# LGPL-3.0
PERMIT_PACKAGE =	Yes

SITES =			https://www.arcane-labs.net/download/OpenBSD/

HOMEPAGE =		https://github.com/gnuradio/volk

WANTLIB += 		${COMPILER_LIBCXX} c m orc-0.4

COMPILER =		base-clang ports-gcc base-gcc

MODULES =		devel/cmake \
			lang/python

BUILD_DEPENDS =		devel/git \
			www/py-mako${MODPY_FLAVOR} \
			devel/orc
			
RUN_DEPENDS =		devel/orc

#CONFIGURE_ARGS =	-DENABLE_DOXYGEN=OFF \
#			-DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=ON 

.include <bsd.port.mk>
