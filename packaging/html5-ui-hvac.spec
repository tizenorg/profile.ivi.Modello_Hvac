Name:       html5_UI_Hvac
Summary:    A proof of concept pure html5 UI
Version:    0.0.1
Release:    1
Group:      Applications/System
License:    Apache 2.0
URL:        http://www.tizen.org
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  zip
Requires:   html5_UI_Common
Requires:   wrt-installer
Requires:   wrt-plugins-ivi
Requires:   wrt-plugins-tizen-bt

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build

make wgtPkg

%install
rm -rf %{buildroot}
%make_install

%post
    wrt-installer -i /opt/usr/apps/.preinstallWidgets/html5UIHvac.wgt;
    cp -r /opt/usr/apps/_common/js/services /opt/usr/apps/html5POC06/res/wgt/js/
    cp -r /opt/usr/apps/_common/css /opt/usr/apps/html5POC06/res/wgt/

%postun
    wrt-installer -un html5POC06.Hvac

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/html5UIHvac.wgt
