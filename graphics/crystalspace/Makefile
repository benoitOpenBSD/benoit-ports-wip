# $OpenBSD$

#ONLY_FOR_ARCHS =	???
#NOT_FOR_ARCHS =	???
#SHARED_ONLY =		???
#COMES_WITH =		???
#BROKEN =		reason

COMMENT =		cross-platform sdk for realtime 3D graphics

DISTNAME =		crystalspace-src-1.2.1
PKGNAME =		${DISTNAME:S/-src//}

#SHARED_LIBS =		???

CATEGORIES =		graphics

HOMEPAGE =		http://downloads.sourceforge.net/crystal/crystalspace-src-1.2.1.tar.bz2?big_mirror=1

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPLv.2.1
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB =		???

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=crystal/}

EXTRACT_SUFX =		.tar.bz2

MODULES	+=		gcc4
MODGCC4_ARCHES =	*

#MODULES =		???
#BUILD_DEPENDS =	???
#RUN_DEPENDS =		???
LIB_DEPENDS =		lcms.>=2.0::graphics/lcms \
			mng::graphics/libmng
#REGRESS_DEPENDS =	???
BUILD_DEPENDS =		::devel/jam

#MAKE_FLAGS =		???
#MAKE_ENV =		???
#FAKE_FLAGS =		???
#REGRESS_FLAGS =	???

USE_X11 =		Yes
USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
#CONFIGURE_STYLE =	autoconf
#CONFIGURE_SCRIPT =	??? (if other than configure)
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--without-java \
			--with-x \
			--with-z \
			--with-png \
			--with-jpeg \
			--with-lcms \
			--with-mng \
			--with-ogg \
			--with-vorbis \
			--with-vorbisfile \
			--with-freetype2
CONFIGURE_ENV =		CPPFLAGS="${CXXFLAGS} -I${LOCALBASE}/include -I${X11BASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib" \
			cs_cv_prog_cxx_visibility_inlines_hidden_supported=no \
			cs_cv_prog_cxx_visibility_inlines_hidden_buggy=yes \
			cs_cv_prog_c_visibility_hidden_ok=no

# for gnu stuff
#AUTOCONF_VERSION =	2.61
#AUTOMAKE_VERSION =	??? (defaults to 1.4)
#MODGNU_CONFIG_GUESS_DIRS = ??? (defaults to ${WRKSRC}

NO_TEST =		Yes

.include <bsd.port.mk>
