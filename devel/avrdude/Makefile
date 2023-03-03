# $OpenBSD: Makefile,v 1.22 2014/06/23 18:15:03 nigel Exp $

COMMENT=	AVR microcontroller hardware in-system programmer

V =		7.1
DISTNAME=	avrdude-${V}
CATEGORIES=	devel
GH_ACCOUNT =	avrdudes
GH_PROJECT =	avrdude
GH_TAGNAME =	v7.1

HOMEPAGE=	http://www.nongnu.org/avrdude/

# GPLv2+
PERMIT_PACKAGE =	Yes

WANTLIB += 	c ftdi1 m ncurses pthread readline
WANTLIB +=	usb usb-1.0 curses elf hidapi-libusb

MODULES =		devel/cmake

USE_GMAKE =		Yes

CFLAGS +=		-I${LOCALBASE}/include

LIB_DEPENDS =		devel/libftdi1 \
			devel/libusb-compat \
			comms/libhidapi

SUBST_VARS +=		V

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/avrdude
	cp -r ${WRKSRC}/atmel-docs/* \
		${PREFIX}/share/doc/avrdude

.include <bsd.port.mk>
