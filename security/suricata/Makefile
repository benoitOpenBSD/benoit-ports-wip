# $OpenBSD$

COMMENT =		Open Source Next Generation Intrusion Detection and Prevention Engine

DISTNAME =		suricata-1.1
CATEGORIES =		security
#SHARED_LIBS +=		yara	0.0	# .1.1

HOMEPAGE =              http://www.openinfosecfoundation.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://www.openinfosecfoundation.org/download/

WANTLIB =		c m stdc++ pcre

LIB_DEPENDS =		devel/pcre

USE_GMAKE =		Yes
USE_GROFF =		Yes
USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_REGRESS =		Yes

.include <bsd.port.mk>
