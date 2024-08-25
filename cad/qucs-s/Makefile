COMMENT =	circuit simulation program

V =		24.3.0
DISTNAME =	qucs-s-${V}

CATEGORIES =	cad

HOMEPAGE =	https://ra3xdh.github.io/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE=	Yes

WANTLIB +=	${COMPILER_LIBCXX} ICE Qt5Core Qt5DBus Qt5Gui Qt5Widgets
WANTLIB +=	Qt5X11Extras SM X11 Xext c m

SITES =		https://github.com/ra3xdh/qucs_s/releases/download/${V}/

MODULES =	devel/cmake \
		x11/qt5

LIB_DEPENDS =	x11/qt5/qtx11extras

RUN_DEPENDS =	cad/ngspice

BUILD_DEPENDS =	devel/bison \
		devel/ninja

.include <bsd.port.mk>
