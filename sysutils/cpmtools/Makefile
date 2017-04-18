# $OpenBSD$

COMMENT =	access CP/M file systems

DISTNAME =	cpmtools-2.20
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

CATEGORIES =	sysutils

HOMEPAGE =	http://www.moria.de/~michael/cpmtools/
MASTER_SITES =	http://www.moria.de/~michael/cpmtools/files/

# GPLv3
PERMIT_PACKAGE_CDROM =	Yes

#WANTLIB +=		c glib-2.0 intl sigrok sigrokdecode

#LIB_DEPENDS =		devel/glib2 \
#			sysutils/libsigrok \
#			sysutils/libsigrokdecode

#MODULES +=		gcc4
#MODGCC4_ARCHS =		*
#MODGCC4_LANGS =		c

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--mandir='${PREFIX}/man' --prefix=${PREFIX}

.include <bsd.port.mk>
