Name     : busybox
Version  : 1.26.2
Release  : 7
URL      : https://busybox.net/downloads/busybox-1.26.2.tar.bz2
Source0  : https://busybox.net/downloads/busybox-1.26.2.tar.bz2
Source1  : config
Summary  : Statically linked binary providing simplified versions of system commands
Group    : Development/Tools
License  : GPL-2.0 bzip2-1.0.6

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%prep
%setup -q -n busybox-1.26.2
cp %{SOURCE1} .config

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489792572
make

%install
export SOURCE_DATE_EPOCH=1489792572
rm -rf %{buildroot}
%make_install CONFIG_PREFIX=%{buildroot}/usr/share/busybox
mv %{buildroot}/usr/share/busybox/sbin/ifconfig %{buildroot}/usr/share/busybox/bin
mv %{buildroot}/usr/share/busybox/sbin/route %{buildroot}/usr/share/busybox/bin
mv %{buildroot}/usr/share/busybox/sbin/udhcpc %{buildroot}/usr/share/busybox/bin
mv %{buildroot}/usr/share/busybox/usr/bin/[ %{buildroot}/usr/share/busybox/bin
mv %{buildroot}/usr/share/busybox/usr/bin/readlink %{buildroot}/usr/share/busybox/bin
mv %{buildroot}/usr/share/busybox/usr/bin/unit %{buildroot}/usr/share/busybox/bin

%files
%defattr(-,root,root,-)
/usr/share/busybox/bin/[
/usr/share/busybox/bin/ash
/usr/share/busybox/bin/busybox
/usr/share/busybox/bin/ifconfig
/usr/share/busybox/bin/ls
/usr/share/busybox/bin/mkdir
/usr/share/busybox/bin/mount
/usr/share/busybox/bin/mv
/usr/share/busybox/bin/ps
/usr/share/busybox/bin/route
/usr/share/busybox/bin/readlink
/usr/share/busybox/bin/sh
/usr/share/busybox/bin/udhcpc
/usr/share/busybox/bin/uname
/usr/share/busybox/bin/unit
