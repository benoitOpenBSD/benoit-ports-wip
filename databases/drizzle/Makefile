# $OpenBSD$

COMMENT =		A Lightweight SQL Database for Cloud and Web

DISTNAME =		drizzle-2009.12.1240

#SHARED_LIBS =		???

CATEGORIES =		databases

HOMEPAGE =		https://launchpad.net/drizzle

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		z pthread readline

MASTER_SITES =		http://launchpad.net/drizzle/trunk/bell/+download/

MODULES+=	devel/gettext
MODULES+=       gcc4

MODGCC4_ARCHES= *
MODGCC4_LANGS=  c c++

BUILD_DEPENDS +=	devel/bison
BUILD_DEPENDS +=	devel/gperf
#RUN_DEPENDS =		???
LIB_DEPENDS +=		pcre.>=2.0::devel/pcre
LIB_DEPENDS +=		lib/uuid/uuid::sysutils/e2fsprogs,-uuid
LIB_DEPENDS +=		curl.>=13::net/curl
LIB_DEPENDS +=		gnutls::security/gnutls
LIB_DEPENDS +=		protobuf::devel/protobuf
LIB_DEPENDS +=		drizzle::databases/libdrizzle
LIB_DEPENDS +=		estdc++.>=11:libstdc++->=4.2,<4.3|libstdc++->=4.2v0,<4.3v0:lang/gcc/4.2,-estdc
#REGRESS_DEPENDS =	???

USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
#CONFIGURE_STYLE =	autoconf autoreconf
#AUTOCONF_VERSION =	2.62

CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--disable-libmemcached \
			--disable-mtmalloc \
			--disable-rpath
CONFIGURE_ENV =		CPPFLAGS='-I${LOCALBASE}/include -I${LOCALBASE}/include/libdrizzle' \
                        LDFLAGS='-L${LOCALBASE}/lib' \
                        ac_cv_libprotobuf=yes
#                        CFLAGS='${CFLAGS}' CXXFLAGS='${CXXFLAGS}'

# for gnu stuff
#AUTOCONF_VERSION =	??? (defaults to 2.13)
#AUTOMAKE_VERSION =	??? (defaults to 1.4)
#MODGNU_CONFIG_GUESS_DIRS = ??? (defaults to ${WRKSRC}

NO_REGRESS =		Yes

# Overrides for default values
#
#CFLAGS =		???
#LDFLAGS =		???
#MAKE_FILE =		???
#PKG_ARCH =		???
#WRKDIST =		??? if other than ${WRKDIR}/$DISTNAME
#WRKSRC =		??? if other than ${WRKDIST}
#WRKBUILD =		??? if other than ${WRKSRC}
#WRKCONF =		??? if other than ${WRKBUILD}

#ALL_TARGET =		???
#INSTALL_TARGET =	???
#REGRESS_TARGET =	???

.include <bsd.port.mk>
