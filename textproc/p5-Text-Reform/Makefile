# $OpenBSD: Makefile,v 1.10 2010/12/03 11:46:49 ajacoutot Exp $

COMMENT=		perl module to formating plaintext

MODULES=		cpan
DISTNAME=		Text-Reform-1.20
CATEGORIES=		textproc
USE_GROFF =		Yes

MAINTAINER=		Sam Smith <s@msmith.net>

# Artistic
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

DEMOS_DIR =	${PREFIX}/share/examples/p5-Text-Reform

post-install:
	${INSTALL_DATA_DIR} ${DEMOS_DIR}
	@cd ${WRKSRC}/demo/ && pax -rw . ${DEMOS_DIR}
	chown -R ${SHAREOWN}:${SHAREGRP} ${DEMOS_DIR}
                    
.include <bsd.port.mk>
