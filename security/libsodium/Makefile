# $OpenBSD$

COMMENT =	library for network communication, encryption, etc

V =		0.1
DISTNAME =	libsodium-${V}
CATEGORIES = 	security

SHARED_LIBS +=	sodium	0.0 # 0.0

HOMEPAGE =	https://github.com/jedisct1/libsodium
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_DISTFILES_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_PACKAGE_CDROM =		Yes

MASTER_SITES =	http://download.dnscrypt.org/libsodium/releases/

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
