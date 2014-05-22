PROJECT = Modello_Hvac

VERSION := 0.0.2
PACKAGE = $(PROJECT)-$(VERSION)

INSTALL_FILES = $(PROJECT).wgt
INSTALL_DIR = ${DESTDIR}/opt/usr/apps/.preinstallWidgets

wgtPkg:
	zip -r $(PROJECT).wgt config.xml css HVAC_icon.png index.html js

install:
	@echo "Installing HVAC, stand by..."
	mkdir -p $(INSTALL_DIR)/
	mkdir -p ${DESTDIR}/opt/usr/apps/_common/icons
	cp $(PROJECT).wgt $(INSTALL_DIR)/
	cp HVAC_icon.png ${DESTDIR}/opt/usr/apps/_common/icons

dist:
	tar czf ../$(PACKAGE).tar.bz2 .
