# $OpenBSD$

COMMENT =	basic hardware access driver library

DISTNAME =	libsigrok-0.4.0
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

SHARED_LIBS +=	sigrok		0.0	# 1.0
SHARED_LIBS +=	sigrokcxx	0.0	# 3.0

CATEGORIES =	sysutils

HOMEPAGE =	https://sigrok.org/wiki/Libsigrok
MASTER_SITES =	http://sigrok.org/download/source/libsigrok/

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		ffi ftdi glib-2.0 gmodule-2.0 gobject-2.0 iconv intl
WANTLIB +=		m pcre pthread python2.7 serialport usb usb-1.0 z
WANTLIB +=		glibmm-2.4 sigc-2.0 zip

CONFIGURE_ARGS +=	--enable-python

BUILD_DEPENDS =		devel/swig \
			devel/doxygen
LIB_DEPENDS =		comms/libserialport \
			devel/libusb1 \
			devel/libftdi \
			devel/glib2 \
			devel/glib2mm \
			archivers/libzip

MODULES +=		lang/python

MODULES +=		gcc4
MODGCC4_ARCHS =		*
MODGCC4_LANGS =		c++

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
