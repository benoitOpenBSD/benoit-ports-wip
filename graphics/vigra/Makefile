# $OpenBSD$

COMMENT=	Computer Vision Library

DISTNAME=	vigra1.6.0
PKGNAME=        vigra-1.6.0
#PKGNAME=        ${DISTNAME:S/_/-/}p0

#SHARED_LIBS=	gif	5.4 \
#		ungif	5.4
CATEGORIES=	graphics

MASTER_SITES=	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/

HOMEPAGE=	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/

MAINTAINER=     Benoit Lecocq <blq@arcane-labs.net>

#
PERMIT_PACKAGE_CDROM=	Yes

WANTLIB=		c m z

LIB_DEPENDS=		tiff.>=35::graphics/tiff \
			fftw3.>=4::math/fftw3 \
			png.>=5.::graphics/png \
			jpeg.>=62.::graphics/jpeg

USE_LIBTOOL=		Yes
USE_GMAKE=		Yes
CONFIGURE_STYLE=	gnu
#CONFIGURE_STYLE=	autoconf

AUTOCONF_VERSION=	2.61
AUTOMAKE_VERSION=	1.9

MAKE_ENV+=		CFLAGS="${CFLAGS}" CC=${CC} CXX=${CXX}
#			SYSCONFDIR="$(SYSCONFDIR)"

CONFIGURE_ARGS+=	 ${CONFIGURE_SHARED} \
			--with-tiff --with-zlib \
			--with-jpeg --with-png \
			--without-boostpython

#CONFIGURE_ENV=		PKG_CONFIG_PATH="${LOCALBASE}/lib/pkgconfig"
#BUILD_DEPENDS=		:autoconf-${AUTOCONF_VERSION}:devel/autoconf/${AUTOCONF_VERSION}

NO_TEST =     Yes

#pre-configure:
#			@cd ${WRKSRC}/config \
#			&& ${SETENV} AUTOMAKE_VERSION=${AUTOMAKE_VERSION} AUTOCONF_VERSION=${AUTOCONF_VERSION} aclocal --acdir=. \
#			&& ${SETENV} AUTOCONF_VERSION=${AUTOCONF_VERSION} AUTOMAKE_VERSION=${AUTOMAKE_VERSION} autoconf \
#			&& mv ${WRKSRC}/config/configure ${WRKSRC}/
                                                                                                			
.include <bsd.port.mk>

# && ${SETENV} AUTOMAKE_VERSION=${AUTOMAKE_VERSION} AUTOCONF_VERSION=${AUTOCONF_VERSION} automake \
# && ${SETENV} AUTOCONF_VERSION=${AUTOCONF_VERSION} AUTOMAKE_VERSION=${AUTOMAKE_VERSION} autoheader \
