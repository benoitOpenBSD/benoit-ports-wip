# $OpenBSD$

COMMENT =	command-line frontend for sigrok

DISTNAME =	sigrok-cli-0.6.0
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

CATEGORIES =	sysutils

HOMEPAGE =	https://sigrok.org/wiki/Sigrok-cli
MASTER_SITES =	http://sigrok.org/download/source/sigrok-cli/

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=		c glib-2.0 intl sigrok sigrokdecode

LIB_DEPENDS =		devel/glib2 \
			sysutils/libsigrok \
			sysutils/libsigrokdecode

MODULES +=		gcc4
MODGCC4_ARCHS =		*
MODGCC4_LANGS =		c

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
