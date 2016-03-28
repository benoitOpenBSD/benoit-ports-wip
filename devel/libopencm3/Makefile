# $OpenBSD$

COMMENT =		firmware library for various ARM Cortex microcontrollers

DISTNAME =		libopencm3-20160315
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv3
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		http://libopencm3.org/wiki/Main_Page

GH_ACCOUNT =		libopencm3
GH_PROJECT =		libopencm3
GH_COMMIT =		492a943b7e448469cd8e88f60fda41ef46aa3b2a

# WANTLIB +=		c m

USE_GMAKE =		Yes

MODULES =		lang/python
BUILD_DEPENDS +=	lang/python/${MODPY_DEFAULT_VERSION_2}
# BUILD_DEPENDS =		devel/arm-none-eabi/gcc-linaro \
#			devel/arm-none-eabi/binutils

pre-build:
	@perl -pi -e 's,/usr/bin/python,${MODPY_BIN},' ${WRKSRC}/scripts/lpcvtcksum
	@perl -pi -e 's,/usr/bin/env python,${MODPY_BIN},' ${WRKSRC}/scripts/irq2nvic_h 

do-build:
	cd ${WRKBUILD} && ${GMAKE}

NO_TEST =		Yes

.include <bsd.port.mk>
