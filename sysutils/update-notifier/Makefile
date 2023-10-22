
COMMENT =	systray icon showing newer OpenBSD snapshots

DISTNAME =	update-notifier-0.3
CATEGORIES =	sysutils

MAINTAINER =	Landry Breuil <gaston@gcu.info>

# BSD
PERMIT_PACKAGE_CDROM =	Yes

SITES =		http://rhaalovely.net/stuff/

NO_BUILD=	yes
NO_REGRESS=	yes

RUN_DEPENDS=	x11/p5-Gtk2 \
		net/p5-Net-SFTP-Foreign \
		www/p5-WWW-IndexParser \
		devel/p5-Config-Tiny

PKG_ARCH=	*

do-install:
	${INSTALL_SCRIPT} ${WRKSRC}/update-notifier.pl \
		${PREFIX}/bin/update-notifier
	${INSTALL_DATA_DIR} ${PREFIX}/share/{doc,examples}/update-notifier
	${INSTALL_DATA} ${WRKSRC}/README ${PREFIX}/share/doc/update-notifier
	${SUBST_CMD} ${WRKSRC}/update-notifier.desktop
	${INSTALL_DATA} ${WRKSRC}/update-notifier.desktop \
		${PREFIX}/share/examples/update-notifier

.include <bsd.port.mk>
