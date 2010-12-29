# $OpenBSD: Makefile,v 1.145 2010/07/25 21:18:34 landry Exp $

COMMENT =	Mozilla web browser

# Don't forget to bump www/firefox-i18n after updates.
MOZILLA_VERSION =	4.0b7
MOZILLA_BRANCH =	2.0b7
MOZILLA_PROJECT =	mozilla-firefox
MOZILLA_CODENAME =	browser

SO_VERSION =	22.0
# NOTE: Must bump minor version if any shlib's are removed from the
# components dir to avoid pkg_add -r issues.
MOZILLA_LIBS =	browsercomps mozalloc mozsqlite3 \
		xpcom xul

CATEGORIES =	www

# mozilla public license
PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

# needed for convert xpm icon to png
BUILD_DEPENDS +=	graphics/netpbm

# lots of logic in mozilla.port.mk
MODULES =	www/mozilla devel/gettext lang/python

MODPY_RUNDEP =	No

USE_X11 =	Yes
# Regression tests are too hard to adapt to run here
NO_REGRESS =	Yes

CONFIGURE_STYLE =	autoconf no-autoheader
CONFIGURE_ARGS +=	--enable-official-branding --disable-install-strip
CONFIGURE_ARGS +=	--with-system-libevent=/usr/
CONFIGURE_ARGS +=	--with-system-zlib=/usr/ --with-system-bz2=${LOCALBASE}
WANTLIB +=	event
#FLAVOR =	debug
#CONFIGURE_ARGS +=	--enable-system-sqlite
# no system sqlite : wants -DSQLITE_ENABLE_UNLOCK_NOTIFY -DSQLITE_SECURE_DELETE
#LIB_DEPENDS +=		:sqlite3->=3.6.23.1:databases/sqlite3
#WANTLIB +=		sqlite3.>=13.3
# --with-system-png=${LOCALBASE}
# no system png : apng support not bundled in

MOZILLA_AUTOCONF_DIRS +=	js/src
MOZILLA_SUBST_FILES +=		config/autoconf.mk.in

SUBST_VARS +=	MOZILLA_VERSION

# remove file that confuses make update-patches
#pre-patch:
#	rm ${WRKSRC}/toolkit/mozapps/extensions/test/unit/*.orig

post-install:
	# override with our own default settings
	${INSTALL_DATA} ${FILESDIR}/browserconfig.properties \
		${PREFIX}/lib/firefox-${MOZILLA_VERSION}/chrome/en-US/locale/branding/
	${SUBST_CMD} -o ${SHAREOWN} -g ${SHAREGRP} -c ${FILESDIR}/mozilla-firefox.1 \
		${PREFIX}/man/man1/mozilla-firefox.1
	cd ${PREFIX}/man/man1/ && ln -sf mozilla-firefox.1 firefox.1
	cd ${PREFIX}/bin/ && ln -sf firefox mozilla-firefox
	# install desktop file
	${INSTALL_DATA_DIR} ${PREFIX}/share/applications/ ; \
	${SUBST_CMD} -o ${SHAREOWN} -g ${SHAREGRP} -c ${FILESDIR}/${_MOZ_PROJECT_SHORT}.desktop \
		${PREFIX}/share/applications/${_MOZ_PROJECT_SHORT}.desktop ; \
	# create an xpm icon from the png one as nsWindow::SetWindowIconList
	# fails to load png icons : confuses the png pixbuf loader from gtk, which
	# differs from the libpng bundled in firefox
	cd ${PREFIX}/lib/firefox-${MOZILLA_VERSION}/chrome/icons/default/ && \
		${LOCALBASE}/bin/pngtopnm -alpha default48.png > ${WRKSRC}/alpha.pgm && \
		${LOCALBASE}/bin/pngtopnm default48.png | \
		${LOCALBASE}/bin/ppmtoxpm -alphamask=${WRKSRC}/alpha.pgm > default.xpm

.include <bsd.port.mk>
