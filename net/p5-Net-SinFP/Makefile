
COMMENT =	a full operating system stack fingerprinting suite

DISTNAME =	Net-SinFP-2.09
CATEGORIES =	net

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl artistic license
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		cpan

BUILD_DEPENDS =		${RUN_DEPENDS}
RUN_DEPENDS =		devel/p5-Class-Gomor \
			net/p5-Net-Packet \
			net/p5-Net-Packet-Target \
			databases/p5-DBIx-SQLite-Simple
  
MODCPAN_EXAMPLES =	Yes

.include <bsd.port.mk>
