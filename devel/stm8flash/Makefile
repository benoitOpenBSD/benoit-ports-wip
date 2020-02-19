# $OpenBSD$

COMMENT =	program your stm8 devices with SWIM/stlinkv(1,2)

DISTNAME =	stm8flash-191006
CATEGORIES =	devel

HOMEPAGE =	https://github.com/vdudouyt/stm8flash

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

GH_ACCOUNT =	vdudouyt
GH_PROJECT =	stm8flash
GH_COMMIT =	3ad9500a04c21f08182439425b19d900c2315217

WANTLIB +=	c usb-1.0 pthread

USE_GMAKE =	Yes

LIB_DEPENDS =	devel/libusb1

NO_TEST =	Yes

.include <bsd.port.mk>
