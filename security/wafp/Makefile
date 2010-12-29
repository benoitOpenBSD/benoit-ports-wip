# $OpenBSD$

COMMENT =		???

DISTNAME =		wafp-0.01-26c3
CATEGORIES =		security

HOMEPAGE =		http://mytty.org/wafp/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

#WANTLIB =		???

MASTER_SITES =		http://mytty.org/wafp/

MODULES =		lang/ruby
#BUILD_DEPENDS =	???
#RUN_DEPENDS =		???
LIB_DEPENDS =		sqlite3::databases/sqlite3 \
			::databases/ruby-sqlite3
#REGRESS_DEPENDS =	???

#MAKE_FLAGS =		???
#MAKE_ENV =		???
#FAKE_FLAGS =		???
#REGRESS_FLAGS =	???

# build/configuration variables
#
#SEPARATE_BUILD =	concurrent  (build simultaneously on all arches)
#SEPARATE_BUILD =	simple  (configure/build still recreates files in source)
#USE_X11 =		Yes
#USE_GMAKE =		Yes
# Programs that uses libtool should use this option,
# unless there is a really good reason not to.
#USE_LIBTOOL =		Yes
# Set CONFIGURE_STYLE to value corresponding to some standard configuration
# 	  perl [modbuild]: perl's MakeMaker Makefile.PL (modbuild: perl's
#	  Module::Build Build.PL)
# 	  gnu [autoconf] [old] [dest]: gnu style configure (old: no
# 	  sysconfdir), (dest: add DESTDIR, does not handle it),
# 	  (autoconf: needed by port, implies gnu)
# 	XXX: cygnus products do NOT use autoconf for making the main
# 		configure from configure.in
# 	  imake [noman]: port uses imake for configuration.
#   	  (noman: no man page installation)
# 	  simple: port has its own configure script
#CONFIGURE_STYLE =	ruby setup
#CONFIGURE_SCRIPT =	??? (if other than configure)
#CONFIGURE_ARGS +=	${CONFIGURE_SHARED}
#CONFIGURE_ENV =	???

# for gnu stuff
#AUTOCONF_VERSION =	??? (defaults to 2.13)
#AUTOMAKE_VERSION =	??? (defaults to 1.4)
#MODGNU_CONFIG_GUESS_DIRS = ??? (defaults to ${WRKSRC}

NO_BUILD =		Yes
NO_REGRESS =		Yes

# Overrides for default values
#
#CFLAGS =		???
#LDFLAGS =		???
#MAKE_FILE =		???
#PKG_ARCH =		???
#WRKDIST =		??? if other than ${WRKDIR}/$DISTNAME
#WRKSRC =		??? if other than ${WRKDIST}
#WRKBUILD =		??? if other than ${WRKSRC}
#WRKCONF =		??? if other than ${WRKBUILD}

#ALL_TARGET =		???
#INSTALL_TARGET =	???
#REGRESS_TARGET =	???

pre-configure:
		${SUBST_CMD} ${WRKSRC}/wafp.rb ${WRKSRC}/lib/wafp_https.rb
                        
do-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp/utils
		${INSTALL_DATA_DIR} ${PREFIX}/share/wafp/lib
		${INSTALL_DATA} ${WRKSRC}/utils/* ${PREFIX}/share/wafp/utils
		${INSTALL_DATA} ${WRKSRC}/lib/* ${PREFIX}/share/wafp/lib
		${INSTALL_DATA} ${WRKSRC}/*.db ${PREFIX}/share/wafp
		${INSTALL_SCRIPT} ${WRKSRC}/wafp.rb ${PREFIX}/bin

.include <bsd.port.mk>
