# $OpenBSD$

COMMENT =		Network authentication cracking tool

DISTNAME =		ncrack-0.7
CATEGORIES =		security

HOMEPAGE =              http://ncrack.org

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MASTER_SITES =		http://nmap.org/ncrack/dist/

WANTLIB =		c m stdc++ ssl crypto

USE_GMAKE =		Yes
USE_GROFF =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS =	--with-localdirs \
			--with-openssl=/usr

NO_TEST =		Yes

.include <bsd.port.mk>
