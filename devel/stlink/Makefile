# $OpenBSD$

COMMENT =	stm32 discovery line programmer

V =		1.5.0
DISTNAME =	stlink-${V}
CATEGORIES =	devel

SHARED_LIBS +=	stlink-shared	0.0

HOMEPAGE =	https://github.com/texane/stlink

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		c usb-1.0

# MASTER_SITES =		http://www.arcane-labs.net/download/OpenBSD/

MASTER_SITES =          ${MASTER_SITES_GITHUB}
GH_ACCOUNT =            texane
GH_PROJECT =            stlink
GH_TAGNAME =            $V

MODULES =		devel/cmake

LIB_DEPENDS =		devel/libusb1

NO_TEST =		Yes

.include <bsd.port.mk>
