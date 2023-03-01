COMMENT =	software development kit for the Raspberry Pi Pico

GH_ACCOUNT =	raspberrypi
GH_PROJECT =	pico-sdk
GH_TAGNAME =	1.5.0
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
MASTER_SITES4 = https://github.com/sekigon-gonnoc/Pico-PIO-USB/archive/

CYW43_V =	38238aefb6f59ce92681d83aa47d3a48d77b2f6e
LWIP_V =	eaf49262393d23842232bafc6ff0a24ee06d8b20
TUSB_V =	34798ff85ec819bafc09da57f7853a1d116a7fff
EX_V =		1c5d9aa567598e6e3eadf6d7f2d8a9342b44dab4
PIO_USB_V =	9ff3f52fd3c1f81532bce8dd311aa8fc8d9b2665

DISTFILES =	${GH_PROJECT}-${GH_TAGNAME}.tar.gz
DISTFILES +=	cyw43-${CYW43_V:C/(........).*/\1/}{${CYW43_V}}.tar.gz:0
DISTFILES +=	lwip-${LWIP_V:C/(........).*/\1/}{${LWIP_V}}.tar.gz:1
DISTFILES +=	tinyusb-${TUSB_V:C/(........).*/\1/}{${TUSB_V}}.tar.gz:2
DISTFILES +=	pico-examples-${EX_V:C/(........).*/\1/}{${EX_V}}.tar.gz:3
DISTFILES +=	Pico-PIO-USB-${PIO_USB_V:C/(........).*/\1/}{${PIO_USB_V}}.tar.gz:4
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
	rmdir ${WRKSRC}/lib/tinyusb/hw/mcu/raspberry_pi/Pico-PIO-USB
	mv ${WRKDIR}/Pico-PIO-USB* ${WRKSRC}/lib/tinyusb/hw/mcu/raspberry_pi/Pico-PIO-USB

do-install:
	@mkdir -p ${INSTALLDIR}
	@cp -r ${WRKSRC}/* ${INSTALLDIR}

post-install:
	${MODPY_BIN} ${MODPY_LIBDIR}/compileall.py \
	    ${PREFIX}/raspberrypi-pico-sdk

.include <bsd.port.mk>
