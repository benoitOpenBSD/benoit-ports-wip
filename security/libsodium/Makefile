# $OpenBSD$

COMMENT =	library for network communication, encryption, etc

V =		0.4.1
DISTNAME =	libsodium-${V}
CATEGORIES = 	security

SHARED_LIBS +=	sodium	0.0 # 1.0

HOMEPAGE =	https://github.com/jedisct1/libsodium
 
MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		http://download.dnscrypt.org/libsodium/releases/

WANTLIB += 		m

CONFIGURE_STYLE =	gnu
#USE_LIBTOOL =		No
                                                
.include <bsd.port.mk>
