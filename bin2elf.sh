#!/usr/bin/env bash
arm-none-eabi-objcopy -I binary -O elf32-littlearm –change-section-address=.data=0x8000000 -B arm -S $1 $2
