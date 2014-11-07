# $OpenBSD: Makefile.template,v 1.71 2014/07/10 12:33:17 sthen Exp $

COMMENT =		???

V =			1.7.1
DISTNAME =		libnfc-${V}

SHARED_LIBS +=  nfc                       0.0 # 5.1

CATEGORIES =		security

HOMEPAGE =		http://nfc-tools.org/index.php?title=Libnfc

#MAINTAINER =		

# GPLv3
PERMIT_PACKAGE_CDROM=Yes

WANTLIB += pthread usb

MASTER_SITES =		http://dl.bintray.com/nfc-tools/sources/
EXTRACT_SUFX =		.tar.bz2

LIB_DEPENDS =		devel/libusb-compat \
			devel/readline

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED}  --with-drivers=acr122_usb,acr122s,pn53x_usb --enable-debug \
			CPPFLAGS="-I${LOCALBASE}/include/ereadline -I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib -pthread" \
			--with-readline=${PREFIX}

.include <bsd.port.mk>
