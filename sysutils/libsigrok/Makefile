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

CONFIGURE_ARGS +=	--enable-python

BUILD_DEPENDS =		devel/swig \
			devel/doxygen
LIB_DEPENDS =		comms/libserialport \
			devel/libusb1 \
			devel/libftdi \
			devel/glib2

MODULES +=		lang/python

MODULES +=		gcc4
MODGCC4_ARCHS =		*
MODGCC4_LANGS =		c++

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
