COMMENT =	circuit simulation program

V =		24.4.0
DISTNAME =	qucs-s-${V}

CATEGORIES =	cad

HOMEPAGE =	https://ra3xdh.github.io/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE=	Yes

WANTLIB +=	${COMPILER_LIBCXX} Qt5Core Qt5Gui Qt5Widgets
WANTLIB +=	Qt5PrintSupport Qt5Svg Qt5Xml c m

SITES =		https://github.com/ra3xdh/qucs_s/releases/download/${V}/

MODULES =	devel/cmake \
		x11/qt5

LIB_DEPENDS =	converters/libiconv \
		x11/qt5/qtsvg \
		x11/qt5/qtcharts

RUN_DEPENDS =	cad/ngspice/ngspice \
		math/gnuplot \
		converters/dos2unix

BUILD_DEPENDS =	devel/bison \
		devel/ninja \
		devel/gperf \
		converters/dos2unix

.include <bsd.port.mk>
