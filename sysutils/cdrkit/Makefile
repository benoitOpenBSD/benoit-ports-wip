# $OpenBSD$

COMMENT =		ISO 9660 filesystem and CD creation tools

DISTNAME =		cdrkit-1.1.9
CATEGORIES =		sysutils

HOMEPAGE =		http://www.cdrkit.org/

MAINTAINER =		James Lecocq <james@james.com>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		c

LIB_DEPENDS =		archivers/bzip2

CONFIGURE_STYLE =       cmake

MODULES +=              devel/cmake \
			devel/gettext

MASTER_SITES =		http://cdrkit.org/releases/

USE_GMAKE =		Yes

MAKE_FLAGS +=		CFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_REGRESS =		Yes

pre-configure:
#		@${SUBST_CMD} ${WRKSRC}/include/CMakeLists.txt
		@${SUBST_CMD} ${WRKSRC}/genisoimage/CMakeLists.txt

.include <bsd.port.mk>
