# $OpenBSD$

COMMENT =	protocol decoding library

DISTNAME =	libsigrokdecode-0.4.1
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

SHARED_LIBS +=	sigrokdecode		0.0	# 3.0

CATEGORIES =	sysutils

HOMEPAGE =	https://sigrok.org/wiki/Libsigrokdecode
MASTER_SITES =	http://sigrok.org/download/source/libsigrokdecode/

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		glib-2.0 iconv intl m pcre pthread util python3.6m

LIB_DEPENDS =		devel/glib2

MODULES +=		lang/python
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

MODULES +=		gcc4
MODGCC4_ARCHS =		*
MODGCC4_LANGS =		c

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
