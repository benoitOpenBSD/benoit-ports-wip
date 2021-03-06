# $OpenBSD: Makefile,v 1.22 2014/06/23 18:15:03 nigel Exp $

COMMENT=	AVR microcontroller hardware in-system programmer

V =		6.3
DISTNAME=	avrdude-${V}
DISTFILES+=	avrdude-${V}.tar.gz avrdude-doc-${V}.pdf
CATEGORIES=	devel

SHARED_LIBS =	avrdude    0.0	# 1.0

HOMEPAGE=	http://www.nongnu.org/avrdude/

# GPLv2+
PERMIT_PACKAGE =	Yes

WANTLIB += 	c ftdi1 m ncurses pthread readline 
WANTLIB +=	termcap usb usb-1.0 curses elf

MASTER_SITES=	${MASTER_SITE_SAVANNAH:=avrdude/}
EXTRACT_ONLY=	avrdude-${V}${EXTRACT_SUFX}

CONFIGURE_STYLE=	gnu
CONFIGURE_ARGS+=	CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib -pthread"

LIB_DEPENDS=		devel/libftdi1 \
			devel/libusb-compat

SUBST_VARS+=		V

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/avrdude
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/avrdude
	${INSTALL_DATA} ${WRKSRC}/avrdude.conf ${PREFIX}/share/examples/avrdude
	${INSTALL_DATA} ${FULLDISTDIR}/avrdude-doc-${V}.pdf \
		${PREFIX}/share/doc/avrdude

.include <bsd.port.mk>
