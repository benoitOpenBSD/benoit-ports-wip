
COMMENT =		tool for inspecting RP2040 binaries

V =			1.1.2
DISTNAME =		picotool-${V}
CATEGORIES =		devel

HOMEPAGE =		https://github.com/raspberrypi/picotool

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# 3 clause BSD
PERMIT_PACKAGE =	Yes

WANTLIB +=		c m usb-1.0 ${COMPILER_LIBCXX}

SITES =                 ${SITES_GITHUB}
GH_ACCOUNT =            raspberrypi
GH_PROJECT =            picotool
GH_TAGNAME =            $V

MODULES =		devel/cmake

LIB_DEPENDS =		devel/libusb1

CONFIGURE_ARGS =	-DPICO_SDK_PATH=${LOCALBASE}/raspberrypi-pico-sdk

NO_TEST =		Yes

.include <bsd.port.mk>
