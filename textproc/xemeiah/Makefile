# $OpenBSD$

COMMENT =		???

DISTNAME =		xemeiah-0.5.4
CATEGORIES =		textproc

HOMEPAGE =		http://sourceforge.net/projects/xemeiah/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		stdc++

MASTER_SITES =		${MASTER_SITE_SOURCEFORGE:=xemeiah/}

EXTRACT_SUFX =		.tar.bz2

# A voir si utile ??
MODULES +=       gcc4
MODGCC4_ARCHES = *
MODGCC4_LANGS =  c++

LIB_DEPENDS =		devel/libmagic \
			archivers/zziplib
MAKE_FLAGS =		CFLAGS="${CFLAGS} -L${LOCALBASE}/lib -I${LOCALBASE}/include -Wall -fPIC -D_FILE_OFFSET_BITS=64"

USE_GMAKE =		Yes

#USE_LIBTOOL =		Yes

NO_TEST =		Yes

WRKSRC =		${WRKDIST}/src

pre-configure:
		${SUBST_CMD} ${WRKSRC}/Config
		
.include <bsd.port.mk>
