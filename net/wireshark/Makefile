# $OpenBSD$

COMMENT =	insecure user-friendly network protocol analyzer

WVER =		1.2.5
DISTNAME =	wireshark-${WVER}
SHARED_LIBS =	wireshark	0.0 \
		wiretap		0.0 \
		wsutil		0.0

CATEGORIES =	net security x11

HOMEPAGE =	http://wireshark.org/

EXTRACT_SUFX =	.tar.bz2

USE_GMAKE =	Yes

# XXX @newuser in pkg/PLIST, not used at present

# Mostly GPLv2 or later. Some files are less restrictive.
# tools/pidl is GPLv3 or later. See COPYING.
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =	c crypto expat jack krb5 m sndio pcap pixman-1 pthread \
		tasn1 z fontconfig freetype X11 Xext Xrender Xau Xcomposite \
		Xcursor Xdamage Xdmcp Xfixes Xi Xinerama Xrandr expat

MASTER_SITES =	http://wireshark.osmirror.nl/download/src/all-versions/ \
		http://www.wireshark.org/download/src/all-versions/ \
		http://wireshark.zing.org/download/src/all-versions/ \
		http://wireshark.cs.pu.edu.tw/download/src/all-versions/

SUBST_VARS =	WVER

# used to create register.c, the shell alternative is slow+semi-broken
MODULES =	lang/python
MODPY_RUNDEP =	no

#BUILD_DEPENDS=	::devel/pkgconfig

LIB_DEPENDS =	devel/atk \
		graphics/cairo \
		net/libcares \
		net/GeoIP \
		x11/gtk+2 \
		devel/glib2 \
		graphics/glitz \
		security/libgcrypt \
		security/libgpg-error \
		security/gnutls \
		converters/libiconv \
		devel/gettext \
		lang/lua \
		devel/pango \
		devel/pcre \
		audio/portaudio-svn \
		graphics/png

USE_LIBTOOL =	Yes

CONFIGURE_STYLE =gnu

CONFIGURE_ARGS =${CONFIGURE_SHARED} \
		--with-adns \
		--with-krb5 \
		--with-net-snmp \
		--with-ssl

CONFIGURE_ENV =	CPPFLAGS="-I/usr/include/kerberosV" \
		LDFLAGS="-Lwiretap/.libs -Lepan/.libs" \
		PYTHON=${MODPY_BIN}

NO_REGRESS =	Yes

# XXX sometimes this gets built empty
pre-install:
	@cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} ${GMAKE} wireshark-filter.4

.include <bsd.port.mk>
