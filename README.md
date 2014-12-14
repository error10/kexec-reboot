# kexec-reboot

Easily choose a kernel to kexec

## Overview

Kexec lets you boot your Linux kernel into another kernel without going through
the hardware reset and reinitialization performed by your system BIOS or
firmware. Since this process can take several minutes, being able to skip it
reduces your downtime.

The problem with kexec is it's an entirely manual process, requiring you to
copy and paste the right kernel, initrd and command line arguments, and hope
you got everything right.

kexec-reboot aims to automate staging a kernel for kexec, so that you can
reboot more quickly and accurately.

## Prerequisites

kexec-reboot requires the following packages to be installed:

 * `kexec-tools` 2.0.0 or higher, for `/sbin/kexec`
 * `ruby` 1.8.7 or higher

In addition, the system must use grub to boot, as kexec-reboot reads the grub
configuration to determine what kernels are available. Both grub 1 and 2
are supported.

## Usage

kexec-reboot accepts the following command line arguments:

 * `-i`, `--interactive`

    Choose the kernel to stage from a list

 * `-l`, `--latest`

    Stage the latest kernel

 * `-r`, `--reboot`

    Reboot immediately after staging the kernel

 * `-v`, `--[no-]verbose`

    Extra verbosity.

After running kexec-reboot, simply reboot your system normally.

## Examples

 * `kexec-reboot -l -r`

   Stage the latest kernel for kexec and reboot immediately.

 * `kexec-reboot -i`

   Show a list of available kernels and select one interactively.
