# $OpenBSD$

COMMENT =		a malware identification and classification tool

DISTNAME =		yara-1.7
CATEGORIES =		security
SHARED_LIBS +=		yara	0.0	# .1.1

HOMEPAGE =              http://code.google.com/p/yara-project/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache 2.0
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://yara-project.googlecode.com/files/

WANTLIB =		c m stdc++ pcre

LIB_DEPENDS =		devel/pcre

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"

NO_TEST =		Yes

.include <bsd.port.mk>
