# $OpenBSD: Makefile,v 1.22 2014/06/23 18:15:03 nigel Exp $

COMMENT=	AVR microcontroller hardware in-system programmer

V =		6.4
DISTNAME=	avrdude-${V}
# DISTFILES+=	avrdude-${V}.tar.gz avrdude-doc-${V}.pdf
CATEGORIES=	devel
GH_ACCOUNT =	avrdudes
GH_PROJECT =	avrdude
GH_TAGNAME =	v6.4


SHARED_LIBS =	avrdude    1.0	# 1.0

HOMEPAGE=	http://www.nongnu.org/avrdude/

# GPLv2+
PERMIT_PACKAGE =	Yes

WANTLIB += 	c ftdi1 m ncurses pthread readline 
WANTLIB +=	termcap usb usb-1.0 curses elf

AUTOCONF_VERSION =	2.69
AUTOMAKE_VERSION =	1.16

USE_GMAKE =		Yes

CONFIGURE_STYLE =	autoreconf
CONFIGURE_ARGS +=	CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib -pthread"

LIB_DEPENDS =		devel/libftdi1 \
			devel/libusb-compat

SUBST_VARS +=		V

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/avrdude
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/avrdude
	${INSTALL_DATA} ${WRKSRC}/avrdude.conf ${PREFIX}/share/examples/avrdude
#	${INSTALL_DATA} ${FULLDISTDIR}/avrdude-doc-${V}.pdf \
#		${PREFIX}/share/doc/avrdude

.include <bsd.port.mk>
