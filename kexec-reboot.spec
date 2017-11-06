Name:		kexec-reboot
Version:	0.8.2
Release:	1%{?dist}
Summary:	Easily choose a kernel to kexec

License:	GPLv3
URL:		https://github.com/error10/kexec-reboot
Source0:	https://github.com/error10/kexec-reboot/archive/%{version}.zip

BuildArch:	noarch

# 2.0.0-203 required on EL6 due to BZ#717637
Requires:	kexec-tools >= 2.0.0-203
Requires:	ruby(release) >= 1.8.7

%description
Kexec lets you boot your Linux kernel into another kernel without going through
the hardware reset and reinitialization performed by your system BIOS or
firmware. Since this process can take several minutes, being able to skip it
reduces your downtime.

kexec-reboot aims to automate staging a kernel for kexec, so that you can
reboot more quickly and accurately.


%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 kexec-reboot %{buildroot}%{_bindir}/kexec-reboot


%files
%doc README.md LICENSE
%{_bindir}/kexec-reboot


%changelog
* Mon Nov  6 2017 Michael Hampton <support@ringingliberty.com> 0.8.2-1
- Initial RPM release.
