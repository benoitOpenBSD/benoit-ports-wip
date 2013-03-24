# $OpenBSD$

COMMENT =	library for network communication, encryption, etc

V =		0.3
DISTNAME =	libsodium-${V}
CATEGORIES = 	security

SHARED_LIBS +=	sodium	0.0 # 1.0

HOMEPAGE =	https://github.com/jedisct1/libsodium
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =	http://download.dnscrypt.org/libsodium/releases/

CONFIGURE_STYLE =	gnu

.include <bsd.port.mk>
