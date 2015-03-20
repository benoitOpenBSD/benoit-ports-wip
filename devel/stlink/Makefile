# $OpenBSD$

COMMENT =	stm32 discovery line programmer

DISTNAME =	stlink-1.0.0.150320
CATEGORIES =	devel

HOMEPAGE =	https://github.com/texane/stlink

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c usb-1.0

MASTER_SITES =		http://www.arcane-labs.net/download/OpenBSD/

AUTOCONF_VERSION =	2.61
AUTOMAKE_VERSION =	1.10
CONFIGURE_STYLE =	gnu

BUILD_DEPENDS =		${MODGNU_AUTOCONF_DEPENDS} \
			${MODGNU_AUTOMAKE_DEPENDS}

LIB_DEPENDS =		devel/libusb1

pre-configure:
	cd ${WRKSRC} && \
	env AUTOMAKE_VERSION=${AUTOMAKE_VERSION} \
	AUTOCONF_VERSION=${AUTOCONF_VERSION} \
		autoreconf -f -i

NO_TEST =		Yes

.include <bsd.port.mk>
