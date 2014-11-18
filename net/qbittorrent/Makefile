# $OpenBSD$

COMMENT =		free and reliable P2P Bittorrent client

DISTNAME =		qbittorrent-2.0.0
CATEGORIES =		net

HOMEPAGE =		http://qbittorrent.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB =		???

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=qbittorrent/}

MODULES +=              x11/qt4
MODULES +=		devel/gettext
#MODULES +=		lang/python

BUILD_DEPENDS +=	devel/boost
BUILD_DEPENDS +=	net/libtorrent-rasterbar

MAKE_FLAGS =		LDFLAGS="-L${LOCALBASE}/lib" \
			CPPFLAGS="${CPPFLAGS} -I${X11BASE}/include" \

USE_GROFF =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

do-configure:
		cd ${WRKSRC} && ./configure --disable-libnotify \
		--with-libboost-inc=${LOCALBASE}/include \
		--disable-geoip-database \
		--qtdir=${MODQT4_QTDIR}
NO_TEST =		Yes

.include <bsd.port.mk>
