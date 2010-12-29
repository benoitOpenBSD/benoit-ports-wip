# $OpenBSD: Makefile,v 1.4 2007/09/16 00:27:06 merdely Exp $

COMMENT=	"berkeley's implementation of the logo programming language"
DISTNAME=	ucblogo-6.0
CATEGORIES=	lang

HOMEPAGE=	http://ucblogo.sourceforge.net/

# BSD
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM= Yes
PERMIT_DISTFILES_FTP=	Yes

WANTLIB=	c m termcap ICE SM X11 pthread stdc++

MASTER_SITES=	http://mirrors.protection.cx/~jolan/ \
		http://www.arcane-labs.net/download/OpenBSD/ 

LIB_DEPENDS=	wx_base,wx_base_net,wx_base_odbc,wx_base_xml,wx_gtk2_adv,wx_gtk2_aui,wx_gtk2_core,wx_gtk2_dbgrid,wx_gtk2_html,wx_gtk2_qa,wx_gtk2_xrc,wx_gtk2_richtext:wxWidgets-gtk2->=2.8.6:x11/wxWidgets

CONFIGURE_STYLE= gnu
CONFIGURE_ARGS+= --with-x
CONFIGURE_ENV=	LDFLAGS="${LDFLAGS} -L${LOCALBASE}/lib -L${X11BASE}/lib"
		          
NO_REGRESS=	Yes

MAKE_FILE=	makefile
ALL_TARGET=	logo makehelp helpfiles helpfiles/HELPCONTENTS

pre-configure:
	@perl -pi -e 's:\@logopath@:${LOCALBASE}/share/ucblogo:g;' \
		${WRKSRC}/init.c
	@perl -pi -e 's:\@logohelp@:${LOCALBASE}/share/ucblogo/helpfiles:g;' \
		${WRKSRC}/init.c

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/ucblogo/helpfiles 
	${INSTALL_DATA} ${WRKSRC}/helpfiles/* ${PREFIX}/share/ucblogo/helpfiles
	${INSTALL_DATA} ${WRKSRC}/Messages ${PREFIX}/share/ucblogo/messages
	${INSTALL_PROGRAM} ${WRKSRC}/logo ${PREFIX}/bin

.include <bsd.port.mk>
