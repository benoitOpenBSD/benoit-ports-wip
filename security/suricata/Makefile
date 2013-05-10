# $OpenBSD$

COMMENT =		Next Generation Intrusion Detection and Prevention Engine

DISTNAME =		suricata-1.4.1
CATEGORIES =		security
SHARED_LIBS +=  htp-0.2                   0.0 # 1.2
SHARED_LIBS +=  htp                       0.0 # 1.2

HOMEPAGE =              http://www.openinfosecfoundation.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://www.openinfosecfoundation.org/download/

WANTLIB =		c pcap pcre pthread yaml-0 z lib/libnet-1.1/net=11 magic

LIB_DEPENDS =		devel/pcre \
			devel/libyaml \
			net/libnet/1.1 \
			devel/libmagic

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
CONFIGURE_ARGS =	--with-libnet-includes=${LOCALBASE}/include/libnet-1.1 \
			--enable-old-barnyard2 \
			--enable-unittests \
			--with-libpcap-includes=/usr/include

NO_TEST =		Yes

.include <bsd.port.mk>
