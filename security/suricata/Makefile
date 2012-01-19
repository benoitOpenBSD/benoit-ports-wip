# $OpenBSD$

COMMENT =		Next Generation Intrusion Detection and Prevention Engine

DISTNAME =		suricata-1.2
CATEGORIES =		security
SHARED_LIBS +=  htp-0.2                   0.0 # 1.2
SHARED_LIBS +=  htp                       0.0 # 1.2

HOMEPAGE =              http://www.openinfosecfoundation.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://www.openinfosecfoundation.org/download/

WANTLIB =		c m stdc++ pcap pcre pthread yaml z lib/libnet-1.1/net=11

LIB_DEPENDS =		devel/pcre \
			devel/libyaml \
			net/libnet/1.1 \
			devel/libmagic

USE_GMAKE =		Yes
USE_GROFF =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
CONFIGURE_ARGS =	--with-libnet-includes=${LOCALBASE}/include/libnet-1.1 \
			--enable-old-barnyard2 \
			--enable-unittests

NO_REGRESS =		Yes

.include <bsd.port.mk>
