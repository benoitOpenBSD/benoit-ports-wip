# $OpenBSD: Makefile,v 1.8 2010/12/03 11:46:47 ajacoutot Exp $

COMMENT=	modular perl shell
CATEGORIES=	shells

V =		0.981
DISTNAME=	Zoidberg-$V
PKGNAME=	zoidberg-$V

# perl
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=	Yes

CPAN_AUTHOR=	JBERGER
MODULES=	cpan
CONFIGURE_STYLE=modbuild
CONFIGURE_ARGS=	install_path=etc="${SYSCONFDIR}/" \
		install_path=doc="${PREFIX}/share/doc/zoid/" \
		install_path=share="${PREFIX}/share/zoid/"
USE_GROFF =	Yes

RUN_DEPENDS=	devel/p5-Exporter-Tidy \
		devel/p5-Term-ReadLine-Zoid \
		devel/p5-Env-PS1 \
		devel/p5-File-ShareDir

BUILD_DEPENDS =	${RUN_DEPENDS}

post-install:
	${INSTALL_DATA_DIR}  ${PREFIX}/share/zoid/pixmaps
	${INSTALL_DATA_DIR}  ${PREFIX}/share/zoid/plugins	
	${INSTALL_DATA} ${WRKSRC}/share/zoidrc.example ${PREFIX}/share/zoid/zoidrc.sample
	${INSTALL_DATA} ${WRKSRC}/share/pixmaps/* ${PREFIX}/share/zoid/pixmaps
	${INSTALL_DATA} ${WRKSRC}/share/plugins/* ${PREFIX}/share/zoid/plugins

.include <bsd.port.mk>
