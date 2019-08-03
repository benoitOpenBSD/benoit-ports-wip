# $OpenBSD$

COMMENT =		firmware library for various ARM Cortex microcontrollers

DISTNAME =		libopencm3-20180306
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv3
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${MASTER_SITES_GITHUB}

HOMEPAGE =		http://libopencm3.org/wiki/Main_Page

GH_ACCOUNT =		libopencm3
GH_PROJECT =		libopencm3
GH_COMMIT =		fb28b4cb7ccc9b157bedf9a506fc893f14a40969

# WANTLIB +=		c m

USE_GMAKE =		Yes

MODULES =		lang/python
BUILD_DEPENDS +=	lang/python/${MODPY_DEFAULT_VERSION_2}
BUILD_DEPENDS =		devel/arm-none-eabi/gcc-linaro \
			devel/arm-none-eabi/binutils

pre-build:
	@perl -pi -e 's,/usr/bin/python,${MODPY_BIN},' ${WRKSRC}/scripts/lpcvtcksum
	@perl -pi -e 's,/usr/bin/env python,${MODPY_BIN},' ${WRKSRC}/scripts/irq2nvic_h 

do-build:
	cd ${WRKBUILD} && ${GMAKE}

NO_TEST =		Yes

.include <bsd.port.mk>
