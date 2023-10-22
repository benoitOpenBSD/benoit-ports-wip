COMMENT =	Open On-Chip Debugging

V =		230226
DISTNAME =	openocd-rp2040-${V}
PKGNAME =	openocd-rp2040
CATEGORIES =	devel

HOMEPAGE =	http://openocd.sourceforge.net/

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB += c ftdi1 hidapi-libusb iconv jim m pthread usb usb-1.0 util

SITES =		https://www.arcane-labs.net/download/OpenBSD/
#GH_ACCOUNT =            raspberrypi
#GH_PROJECT =            openocd

AUTOCONF_VERSION =      2.69
AUTOMAKE_VERSION =      1.16

MAKE_ENV =		AUTOCONF_VERSION="${AUTOCONF_VERSION}" \
			AUTOMAKE_VERSION="${AUTOMAKE_VERSION}"

CONFIGURE_STYLE = autoreconf

CONFIGURE_ARGS = --disable-werror \
		--disable-wextra \
		--disable-internal-jimtcl \
		--without-capstone \
		--disable-internal-libjaylink \
		-enable-picoprobe

CONFIGURE_ENV =	CPPFLAGS="-I${LOCALBASE}/include -I${LOCALBASE}/include/jim" \
		LDFLAGS="-L${LOCALBASE}/lib -pthread"

LIB_DEPENDS =	comms/libhidapi \
		devel/libftdi1 \
		devel/libusb-compat \
		lang/jimtcl>=0.75

WRKDIST=	${WRKDIR}/${PKGNAME}
WRKSRC =	${WRKDIR}/${PKGNAME}
		
USE_GMAKE =	Yes
# Fails to link main.o and libopenocd.a properly resulting in undefined reference in the gdb_server.o
USE_LIBTOOL =	gnu

.include <bsd.port.mk>
