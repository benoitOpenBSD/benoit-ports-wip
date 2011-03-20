# $OpenBSD$

COMMENT =	library for manipulating PDF documents

VERSION =	0.4.5
DISTNAME =	pdfedit-${VERSION}
CATEGORIES =	textproc

HOMEPAGE =	http://pdfedit.petricek.net/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES		= ${MASTER_SITE_SOURCEFORGE:=pdfedit/}

WANTLIB =		c m z stdc++ freetype t1 ICE X11

LIB_DEPENDS =		devel/t1lib \
			devel/boost

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--with-parallel-make=off \
			--enable-tools \
			--enable-pdfedit-core-dev \
			--disable-gui \
			--with-t1-includes=${LOCALBASE}/include \
			--with-t1-library=${LOCALBASE}/lib
#			--enable-poratability-flags=no

#CONFIGURE_ENV = 
#CONFIGURE_ENV += CPPFLAGS='-I${LOCALBASE}/include'
#CONFIGURE_ENV = CPPFLAGS='-I${X11BASE}/include/freetype2 -I${X11BASE}/include -I${LOCALBASE}/include -DLOCALBASE="\"${LOCALBASE}\""' \
#		LDFLAGS="-L${X11BASE}/lib -L${LOCALBASE}/lib -lm -lz"
 
NO_REGRESS =		Yes

.include <bsd.port.mk>
