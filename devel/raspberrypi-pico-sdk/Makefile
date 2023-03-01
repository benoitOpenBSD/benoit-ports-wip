COMMENT =	software development kit for the Raspberry Pi Pico

GH_ACCOUNT =	raspberrypi
GH_PROJECT =	pico-sdk
GH_TAGNAME =	1.4.0
PKGNAME =	${GH_ACCOUNT}-${GH_PROJECT}-${GH_TAGNAME}

CATEGORIES =	devel

MAINTAINER =	Tracey Emery <tracey@openbsd.org>

# BSD-3
PERMIT_PACKAGE = Yes

MODULES =	lang/python

RUN_DEPENDS +=	devel/arm-none-eabi/binutils,arm \
		devel/arm-none-eabi/gcc-linaro,arm \
		devel/arm-none-eabi/newlib,arm

MASTER_SITES0 = https://github.com/georgerobotics/cyw43-driver/archive/
MASTER_SITES1 = https://github.com/lwip-tcpip/lwip/archive/
MASTER_SITES2 = https://github.com/hathach/tinyusb/archive/
MASTER_SITES3 = https://github.com/raspberrypi/pico-examples/archive/

CYW43_V =	195dfcc10bb6f379e3dea45147590db2203d3c7b
LWIP_V =	239918ccc173cb2c2a62f41a40fd893f57faf1d6
TUSB_V =	4bfab30c02279a0530e1a56f4a7c539f2d35a293
EX_V =		a7ad17156bf60842ee55c8f86cd39e9cd7427c1d

DISTFILES =	${GH_PROJECT}-${GH_TAGNAME}.tar.gz
DISTFILES +=	cyw43-${CYW43_V:C/(........).*/\1/}{${CYW43_V}}.tar.gz:0
DISTFILES +=	lwip-${LWIP_V:C/(........).*/\1/}{${LWIP_V}}.tar.gz:1
DISTFILES +=	tinyusb-${TUSB_V:C/(........).*/\1/}{${TUSB_V}}.tar.gz:2
DISTFILES +=	pico-examples-${EX_V:C/(........).*/\1/}{${EX_V}}.tar.gz:3
INSTALLDIR =	${PREFIX}/raspberrypi-pico-sdk

NO_TEST =	Yes
NO_BUILD =	Yes

post-extract:
	rmdir ${WRKSRC}/lib/cyw43-driver
	mv ${WRKDIR}/cyw43* ${WRKSRC}/lib/cyw43-driver
	rmdir ${WRKSRC}/lib/lwip
	mv ${WRKDIR}/lwip* ${WRKSRC}/lib/lwip
	rmdir ${WRKSRC}/lib/tinyusb
	mv ${WRKDIR}/tinyusb* ${WRKSRC}/lib/tinyusb
	mv ${WRKDIR}/pico-examples* ${WRKSRC}/pico-examples

do-install:
	@mkdir -p ${INSTALLDIR}
	@cp -r ${WRKSRC}/* ${INSTALLDIR}

post-install:
	${MODPY_BIN} ${MODPY_LIBDIR}/compileall.py \
	    ${PREFIX}/raspberrypi-pico-sdk

.include <bsd.port.mk>
