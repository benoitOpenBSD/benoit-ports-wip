# $OpenBSD$

SHARED_ONLY =	Yes

COMMENT =	XMPP plugin for irssi

DISTNAME =	irssi-xmpp-0.52
CATEGORIES =	net

HOMEPAGE =	http://cybione.org/~irssi-xmpp
MASTER_SITES =	${HOMEPAGE}/files/

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM = Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB +=	glib-2.0 iconv intl loudmouth-1 idn

LIB_DEPENDS = 	net/loudmouth \
		devel/glib2 \
		devel/libidn

BUILD_DEPENDS =	net/irssi:configure
RUN_DEPENDS =	irssi-*:net/irssi

MAKE_FLAGS += IRSSI_INCLUDE=${WRKDIR}/irssi-src

NO_CONFIGURE = Yes
NO_REGRESS = Yes

post-extract:
	@ln -sf ${WRKDIR}/net/irssi/irssi-* ${WRKDIR}/irssi-src

.include <bsd.port.mk>
