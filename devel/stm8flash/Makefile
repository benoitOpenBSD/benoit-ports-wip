# $OpenBSD$

COMMENT =	program your stm8 devices with SWIM/stlinkv(1,2)

DISTNAME =	stm8flash-190210
CATEGORIES =	devel

HOMEPAGE =	https://github.com/vdudouyt/stm8flash

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

GH_ACCOUNT =	vdudouyt
GH_PROJECT =	stm8flash
GH_COMMIT =	74d013c3e24f535e36f3227a7975d32470af0ae8

WANTLIB +=	c usb-1.0 pthread

USE_GMAKE =	Yes

LIB_DEPENDS =	devel/libusb1

NO_TEST =	Yes

.include <bsd.port.mk>
