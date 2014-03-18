# $OpenBSD$

COMMENT =		the pattern matching swiss knife for malware researchers

Y_VER =			2.1.0
DISTNAME =		yara-${Y_VER}
CATEGORIES =		security
SHARED_LIBS +=		yara	0.0	# .0.0

HOMEPAGE =              http://plusvic.github.io/yara/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache 2.0
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =          https://github.com/plusvic/yara/archive/
DISTFILES =             ${DISTNAME}{${Y_VER}}${EXTRACT_SUFX}

WANTLIB =		c pthread

CONFIGURE_STYLE =	automake
CONFIGURE_ENV =		CPPFLAGS="-I${LOCALBASE}/include" \
			LDFLAGS="-L${LOCALBASE}/lib"
AUTOCONF_VERSION	= 2.69
AUTOMAKE_VERSION	= 1.14

USE_LIBTOOL =		gnu

pre-configure:
			cd ${WRKSRC} && ${SETENV} AUTOMAKE_VERSION=${AUTOMAKE_VERSION} \
			AUTOCONF_VERSION=${AUTOCONF_VERSION} \
			sh ./bootstrap.sh

NO_TEST =		Yes

.include <bsd.port.mk>
