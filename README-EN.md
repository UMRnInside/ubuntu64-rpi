# ubuntu-rpi64

ubuntu-rpi64 is an experimental 64-bit OS for the Raspberry Pi 3. It is based on ubuntu 17.04 and backed by a 4.12.14 Linux kernel.

## About

There are three versions: ubuntu 15.10 , ubuntu 16.04 and ubuntu 17.04.

But the stable version is ubuntu 16.04.3.

## How to install this system?

You can follow this [instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) to write the image to your SD-card.

## How to get started?

The username is `ubuntu`,and password is `ubuntu`.

For root,password is `root`.

Once logged in, you might want to run sudo `raspi-config` or `chainsx-config` in order to get assisted with your setup!

On the lite version, SSH is enabled by default.

## Others

* You can follow this step to enable the 32-bit support.

`sudo dpkg --add-architecture armhf`

`sudo apt-get update`

`sudo apt-get install libc6:armhf`

* This system build is based on ubuntu-Base-17.04

## About

* The system is based on ubuntu-Base-17.04-arm64, not a ported version, so it is stable but incomplete

* It can boot up in **less than 10s** , even faster than official Raspbian Lite and Pi64

* It contains:
    * Linux kernel 4.12.14 from Raspberry Pi Foundation
    * Configs from @UMRnInside
    * Rootfs from ubuntu-Base-arm64

## Note

* Default apt mirror is provided by `mirrors.tuna.tsinghua.edu.cn`
* SSH is **enabled** by default
* Unity is broken, because there is no hardware acceleration available on armhf
* It will **NOT** expand rootfs automatically, which means you need to expand it manually using tools like _fdisk_ or _gparted_
* For anything else...Just contact me, as I am not much experienced.You can contribute this project at your convenience.
* You can find a way to expand a ext4 partition in `Documentation`.

************************
# Download link

|netdisk|link|
|--------|----|
|onedrive|https://1drv.ms/u/s!Aj2tyhuVKq9-c6eH_pbiP2gUnI8|
|yandex.disk|https://yadi.sk/d/ysdTPoeF3R7LCU|
|mega|https://mega.nz/#!wqwUgSrY!5a-0gcJecn9X94_Ahr6g4OBISl7CbFNk_ZJXkKvIHr4|
|sandisk.cloud|https://sandisk.upthere.com/loop/c0fe40d8a0919986d822e8754e0c5553c3049b6ba244f9ee3d0edcdbeecb3a1c|
