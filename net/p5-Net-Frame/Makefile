# $OpenBSD$

COMMENT =	perl base framework for frame crafting 

DISTNAME =	Net-Frame-1.06
CATEGORIES =	net

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl Artistic License
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MODULES =		cpan

BUILD_DEPENDS =		${RUN_DEPENDS}
RUN_DEPENDS =		net/p5-Socket6 \
			math/p5-Bit-Vector \
			net/p5-Net-IPv6Addr \
			devel/p5-Class-Gomor
         
MODCPAN_EXAMPLES =	Yes

.include <bsd.port.mk>
