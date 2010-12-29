# $OpenBSD$

COMMENT =		C library aiming to implement the Liberty Alliance standards

DISTNAME =		lasso-2.2.2
#SHARED_LIBS +=		lasso	0.0	# .10.1
CATEGORIES =		security

HOMEPAGE =		http://lasso.entrouvert.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		c crypto ssl z

MASTER_SITES =		http://labs.libre-entreprise.org/frs/download.php/735/

MODULES +=		devel/gettext 
MODULES +=		lang/python
BUILD_DEPENDS +=	devel/swig
BUILD_DEPENDS +=	textproc/libxslt
LIB_DEPENDS +=		security/xmlsec
LIB_DEPENDS +=		devel/glib2
LIB_DEPENDS +=		security/cyrus-sasl2

USE_GMAKE =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} 
CONFIGURE_ARGS +=	--disable-php4 --disable-php5 --disable-java 
CONFIGURE_ARGS +=	--disable-perl --disable-python
CONFIGURE_ARGS +=	--with-sasl2=/usr/local
#CONFIGURE_ARGS +=	--enable-wsf
CONFIGURE_ENV +=	PKG_CONFIG_PATH=${X11BASE}/lib/pkgconfig

NO_REGRESS =		Yes

.include <bsd.port.mk>
