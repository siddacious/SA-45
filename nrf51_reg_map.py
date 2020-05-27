
#==========================================================================
#==========                      POWER                     ================
#==========================================================================


# IO Type Qualifier	Type	Description
# __IM	Struct member	Defines 'read only' permissions
# __OM	Struct member	Defines 'write only' permissions
# __IOM	Struct member	Defines 'read / write' permissions
# __I	Scalar variable	Defines 'read only' permissions
# __O	Scalar variable	Defines 'write only' permissions
# __IO	Scalar variable	Defines 'read / write' permissions

register_blocks = {
"POWER" : [
  ("R", 4, "RESERVED0", 30),
  ("W", 4, "TASKS_CONSTLAT"),                    # Enable constant latency mode.
  ("W", 4, "TASKS_LOWPWR"),                      # Enable low power mode (variable latency).
  ("R", 4, "RESERVED1", 34),
  ("RW", 4, "EVENTS_POFWARN"),                    # Power failure warning.
  ("R", 4, "RESERVED2", 126),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 61),
  ("RW", 4, "RESETREAS"),                         # Reset reason.
  ("R", 4, "RESERVED4", 9),
  ("R", 4, "RAMSTATUS"),                         # Ram status register.
  ("R", 4, "RESERVED5", 53),
  ("W", 4, "SYSTEMOFF"),                         # System off register.
  ("R", 4, "RESERVED6", 3),
  ("RW", 4, "POFCON"),                            # Power failure configuration.
  ("R", 4, "RESERVED7", 2),
  ("RW", 4, "GPREGRET"),                          # General purpose retention register. This register is a retained register.
  ("R", 4, "RESERVED8"),
  ("RW", 4, "RAMON"),                             # Ram on/off.
  ("R", 4, "RESERVED9", 7),
  ("RW", 4, "RESET"),                             # Pin reset functionality configuration register. This register is a retained register.
  ("R", 4, "RESERVED10", 3),
  ("RW", 4, "RAMONB"),                            # Ram on/off.
  ("R", 4, "RESERVED11", 8),
  ("RW", 4, "DCDCEN"),                            # DCDC converter enable configuration register.
  ("R", 4, "RESERVED12", 291),
  ("RW", 4, "DCDCFORCE"),                         # DCDC power-up force register.
  ("NRF_POWER_Type")
]


#==========================================================================
#==========                      CLOCK                     ================
# @brief Clock control. (CLOCK)
#==========================================================================
,
"CLOCK" : [
  ("W", 4, "TASKS_HFCLKSTART"),                  # Start HFCLK clock source.
  ("W", 4, "TASKS_HFCLKSTOP"),                   # Stop HFCLK clock source.
  ("W", 4, "TASKS_LFCLKSTART"),                  # Start LFCLK clock source.
  ("W", 4, "TASKS_LFCLKSTOP"),                   # Stop LFCLK clock source.
  ("W", 4, "TASKS_CAL"),                         # Start calibration of LFCLK RC oscillator.
  ("W", 4, "TASKS_CTSTART"),                     # Start calibration timer.
  ("W", 4, "TASKS_CTSTOP"),                      # Stop calibration timer.
  ("R", 4, "RESERVED0", 57),
  ("RW", 4, "EVENTS_HFCLKSTARTED"),               # HFCLK oscillator started.
  ("RW", 4, "EVENTS_LFCLKSTARTED"),               # LFCLK oscillator started.
  ("R", 4, "RESERVED1"),
  ("RW", 4, "EVENTS_DONE"),                       # Calibration of LFCLK RC oscillator completed.
  ("RW", 4, "EVENTS_CTTO"),                       # Calibration timer timeout.
  ("R", 4, "RESERVED2", 124),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 63),
  ("R", 4, "HFCLKRUN"),                          # Task HFCLKSTART trigger status.
  ("R", 4, "HFCLKSTAT"),                         # High frequency clock status.
  ("R", 4, "RESERVED4"),
  ("R", 4, "LFCLKRUN"),                          # Task LFCLKSTART triggered status.
  ("R", 4, "LFCLKSTAT"),                         # Low frequency clock status.
  ("R", 4, "LFCLKSRCCOPY"),                      # Clock source for the LFCLK clock, set when task LKCLKSTART is triggered.
  ("R", 4, "RESERVED5", 62),
  ("RW", 4, "LFCLKSRC"),                          # Clock source for the LFCLK clock.
  ("R", 4, "RESERVED6", 7),
  ("RW", 4, "CTIV"),                              # Calibration timer interval.
  ("R", 4, "RESERVED7", 5),
  ("RW", 4, "XTALFREQ"),                          # Crystal frequency.
  ("NRF_CLOCK_Type")
]


#==========================================================================
#==========                       MPU                      ================
# @brief Memory Protection Unit. (MPU)
#==========================================================================
,
"MPU" : [
  ("R", 4, "RESERVED0", 330),
  ("RW", 4, "PERR0"),                             # Configuration of peripherals in mpu regions.
  ("RW", 4, "RLENR0"),                            # Length of RAM region 0.
  ("R", 4, "RESERVED1", 52),
  ("RW", 4, "PROTENSET0"),                        # Erase and write protection bit enable set register.
  ("RW", 4, "PROTENSET1"),                        # Erase and write protection bit enable set register.
  ("RW", 4, "DISABLEINDEBUG"),                    # Disable erase and write protection mechanism in debug mode.
  ("RW", 4, "PROTBLOCKSIZE"),                     # Erase and write protection block size.
  ("NRF_MPU_Type")
],

#==========================================================================
#==========                    RADIO                     ================
# @brief The radio. (RADIO)
#==========================================================================
"RADIO" : [
  ("W", 4, "TASKS_TXEN"),                        # Enable radio in TX mode.
  ("W", 4, "TASKS_RXEN"),                        # Enable radio in RX mode.
  ("W", 4, "TASKS_START"),                       # Start radio.
  ("W", 4, "TASKS_STOP"),                        # Stop radio.
  ("W", 4, "TASKS_DISABLE"),                     # Disable radio.
  ("W", 4, "TASKS_RSSISTART"),                   # Start the RSSI and take one sample of the receive signal strength.
  ("W", 4, "TASKS_RSSISTOP"),                    # Stop the RSSI measurement.
  ("W", 4, "TASKS_BCSTART"),                     # Start the bit counter.
  ("W", 4, "TASKS_BCSTOP"),                      # Stop the bit counter.
  ("R", 4, "RESERVED0", 55),
  ("RW", 4, "EVENTS_READY"),                      # Ready event.
  ("RW", 4, "EVENTS_ADDRESS"),                    # Address event.
  ("RW", 4, "EVENTS_PAYLOAD"),                    # Payload event.
  ("RW", 4, "EVENTS_END"),                        # End event.
  ("RW", 4, "EVENTS_DISABLED"),                   # Disable event.
  ("RW", 4, "EVENTS_DEVMATCH"),                   # A device address match occurred on the last received packet.
  ("RW", 4, "EVENTS_DEVMISS"),                    # No device address match occurred on the last received packet.
  ("RW", 4, "EVENTS_RSSIEND"),                    # Sampling of the receive signal strength complete. A new RSSI sample is ready for readout at the RSSISAMPLE register.
  ("R", 4, "RESERVED1", 2),
  ("RW", 4, "EVENTS_BCMATCH"),                    # Bit counter reached bit count value specified in BCC register.
  ("R", 4, "RESERVED2", 53),
  ("RW", 4, "SHORTS"),                            # Shortcuts for the radio.
  ("R", 4, "RESERVED3", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED4", 61),
  ("R", 4, "CRCSTATUS"),                         # CRC status of received packet.
  ("R", 4, "RESERVED5"),
  ("R", 4, "RXMATCH"),                           # Received address.
  ("R", 4, "RXCRC"),                             # Received CRC.
  ("R", 4, "DAI"),                               # Device address match index.
  ("R", 4, "RESERVED6", 60),
  ("RW", 4, "PACKETPTR"),                         # Packet pointer. Decision point: START task.
  ("RW", 4, "FREQUENCY"),                         # Frequency.
  ("RW", 4, "TXPOWER"),                           # Output power.
  ("RW", 4, "MODE"),                              # Data rate and modulation.
  ("RW", 4, "PCNF0"),                             # Packet configuration 0.
  ("RW", 4, "PCNF1"),                             # Packet configuration 1.
  ("RW", 4, "BASE0"),                             # Radio base address 0. Decision point: START task.
  ("RW", 4, "BASE1"),                             # Radio base address 1. Decision point: START task.
  ("RW", 4, "PREFIX0"),                           # Prefixes bytes for logical addresses 0 to 3.
  ("RW", 4, "PREFIX1"),                           # Prefixes bytes for logical addresses 4 to 7.
  ("RW", 4, "TXADDRESS"),                         # Transmit address select.
  ("RW", 4, "RXADDRESSES"),                       # Receive address select.
  ("RW", 4, "CRCCNF"),                            # CRC configuration.
  ("RW", 4, "CRCPOLY"),                           # CRC polynomial.
  ("RW", 4, "CRCINIT"),                           # CRC initial value.
  ("RW", 4, "TEST"),                              # Test features enable register.
  ("RW", 4, "TIFS"),                              # Inter Frame Spacing in microseconds.
  ("R", 4, "RSSISAMPLE"),                        # RSSI sample.
  ("R", 4, "RESERVED7"),
  ("R", 4, "STATE"),                             # Current radio state.
  ("RW", 4, "DATAWHITEIV"),                       # Data whitening initial value.
  ("R", 4, "RESERVED8", 2),
  ("RW", 4, "BCC"),                               # Bit counter compare.
  ("R", 4, "RESERVED9", 39),
  ("RW", 4, "DAB", 8),                            # Device address base segment.
  ("RW", 4, "DAP", 8),                            # Device address prefix.
  ("RW", 4, "DACNF"),                             # Device address match configuration.
  ("R", 4, "RESERVED10", 56),
  ("RW", 4, "OVERRIDE0"),                         # Trim value override register 0.
  ("RW", 4, "OVERRIDE1"),                         # Trim value override register 1.
  ("RW", 4, "OVERRIDE2"),                         # Trim value override register 2.
  ("RW", 4, "OVERRIDE3"),                         # Trim value override register 3.
  ("RW", 4, "OVERRIDE4"),                         # Trim value override register 4.
  ("R", 4, "RESERVED11", 561),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_RADIO_Type")
]


#==========================================================================
#==========                      UART                      ================
# @brief Universal Asynchronous Receiver/Transmitter. (UART)
#==========================================================================
,
"UART" : [
  ("W", 4, "TASKS_STARTRX"),                     # Start UART receiver.
  ("W", 4, "TASKS_STOPRX"),                      # Stop UART receiver.
  ("W", 4, "TASKS_STARTTX"),                     # Start UART transmitter.
  ("W", 4, "TASKS_STOPTX"),                      # Stop UART transmitter.
  ("R", 4, "RESERVED0", 3),
  ("W", 4, "TASKS_SUSPEND"),                     # Suspend UART.
  ("R", 4, "RESERVED1", 56),
  ("RW", 4, "EVENTS_CTS"),                        # CTS activated.
  ("RW", 4, "EVENTS_NCTS"),                       # CTS deactivated.
  ("RW", 4, "EVENTS_RXDRDY"),                     # Data received in RXD.
  ("R", 4, "RESERVED2", 4),
  ("RW", 4, "EVENTS_TXDRDY"),                     # Data sent from TXD.
  ("R", 4, "RESERVED3"),
  ("RW", 4, "EVENTS_ERROR"),                      # Error detected.
  ("R", 4, "RESERVED4", 7),
  ("RW", 4, "EVENTS_RXTO"),                       # Receiver timeout.
  ("R", 4, "RESERVED5", 46),
  ("RW", 4, "SHORTS"),                            # Shortcuts for UART.
  ("R", 4, "RESERVED6", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED7", 93),
  ("RW", 4, "ERRORSRC"),                          # Error source. Write error field to 1 to clear error.
  ("R", 4, "RESERVED8", 31),
  ("RW", 4, "ENABLE"),                            # Enable UART and acquire IOs.
  ("R", 4, "RESERVED9"),
  ("RW", 4, "PSELRTS"),                           # Pin select for RTS.
  ("RW", 4, "PSELTXD"),                           # Pin select for TXD.
  ("RW", 4, "PSELCTS"),                           # Pin select for CTS.
  ("RW", 4, "PSELRXD"),                           # Pin select for RXD.
  ("R", 4, "RXD"),                               # RXD register. On read action the buffer pointer is displaced. Once read the character is consumed. If read when no character  available, the UART will stop working.
  ("W", 4, "TXD"),                               # TXD register.
  ("R", 4, "RESERVED10"),
  ("RW", 4, "BAUDRATE"),                          # UART Baudrate.
  ("R", 4, "RESERVED11", 17),
  ("RW", 4, "CONFIG"),                            # Configuration of parity and hardware flow control register.
  ("R", 4, "RESERVED12", 675),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_UART_Type")
]


#==========================================================================
#==========                       SPI                      ================
# @brief SPI master 0. (SPI)
#==========================================================================
,
"SPI" : [
  ("R", 4, "RESERVED0", 66),
  ("RW", 4, "EVENTS_READY"),                      # TXD byte sent and RXD byte received.
  ("R", 4, "RESERVED1", 126),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED2", 125),
  ("RW", 4, "ENABLE"),                            # Enable SPI.
  ("R", 4, "RESERVED3"),
  ("RW", 4, "PSELSCK"),                           # Pin select for SCK.
  ("RW", 4, "PSELMOSI"),                          # Pin select for MOSI.
  ("RW", 4, "PSELMISO"),                          # Pin select for MISO.
  ("R", 4, "RESERVED4"),
  ("R", 4, "RXD"),                               # RX data.
  ("RW", 4, "TXD"),                               # TX data.
  ("R", 4, "RESERVED5"),
  ("RW", 4, "FREQUENCY"),                         # SPI frequency
  ("R", 4, "RESERVED6", 11),
  ("RW", 4, "CONFIG"),                            # Configuration register.
  ("R", 4, "RESERVED7", 681),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_SPI_Type")
]


#==========================================================================
#==========                       TWI                      ================
# @brief Two-wire interface master 0. (TWI)
#==========================================================================
,
"TWI" : [
  ("W", 4, "TASKS_STARTRX"),                     # Start 2-Wire master receive sequence.
  ("R", 4, "RESERVED0"),
  ("W", 4, "TASKS_STARTTX"),                     # Start 2-Wire master transmit sequence.
  ("R", 4, "RESERVED1", 2),
  ("W", 4, "TASKS_STOP"),                        # Stop 2-Wire transaction.
  ("R", 4, "RESERVED2"),
  ("W", 4, "TASKS_SUSPEND"),                     # Suspend 2-Wire transaction.
  ("W", 4, "TASKS_RESUME"),                      # Resume 2-Wire transaction.
  ("R", 4, "RESERVED3", 56),
  ("RW", 4, "EVENTS_STOPPED"),                    # Two-wire stopped.
  ("RW", 4, "EVENTS_RXDREADY"),                   # Two-wire ready to deliver new RXD byte received.
  ("R", 4, "RESERVED4", 4),
  ("RW", 4, "EVENTS_TXDSENT"),                    # Two-wire finished sending last TXD byte.
  ("R", 4, "RESERVED5"),
  ("RW", 4, "EVENTS_ERROR"),                      # Two-wire error detected.
  ("R", 4, "RESERVED6", 4),
  ("RW", 4, "EVENTS_BB"),                         # Two-wire byte boundary.
  ("R", 4, "RESERVED7", 3),
  ("RW", 4, "EVENTS_SUSPENDED"),                  # Two-wire suspended.
  ("R", 4, "RESERVED8", 45),
  ("RW", 4, "SHORTS"),                            # Shortcuts for TWI.
  ("R", 4, "RESERVED9", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED10", 110),
  ("RW", 4, "ERRORSRC"),                          # Two-wire error source. Write error field to 1 to clear error.
  ("R", 4, "RESERVED11", 14),
  ("RW", 4, "ENABLE"),                            # Enable two-wire master.
  ("R", 4, "RESERVED12"),
  ("RW", 4, "PSELSCL"),                           # Pin select for SCL.
  ("RW", 4, "PSELSDA"),                           # Pin select for SDA.
  ("R", 4, "RESERVED13", 2),
  ("R", 4, "RXD"),                               # RX data register.
  ("RW", 4, "TXD"),                               # TX data register.
  ("R", 4, "RESERVED14"),
  ("RW", 4, "FREQUENCY"),                         # Two-wire frequency.
  ("R", 4, "RESERVED15", 24),
  ("RW", 4, "ADDRESS"),                           # Address used in the two-wire transfer.
  ("R", 4, "RESERVED16", 668),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_TWI_Type")
]


#==========================================================================
#==========                      SPIS                      ================
# @brief SPI slave 1. (SPIS)
#==========================================================================
,
"SPIS" : [
  ("R", 4, "RESERVED0", 9),
  ("W", 4, "TASKS_ACQUIRE"),                     # Acquire SPI semaphore.
  ("W", 4, "TASKS_RELEASE"),                     # Release SPI semaphore.
  ("R", 4, "RESERVED1", 54),
  ("RW", 4, "EVENTS_END"),                        # Granted transaction completed.
  ("R", 4, "RESERVED2", 2),
  ("RW", 4, "EVENTS_ENDRX"),                      # End of RXD buffer reached
  ("R", 4, "RESERVED3", 5),
  ("RW", 4, "EVENTS_ACQUIRED"),                   # Semaphore acquired.
  ("R", 4, "RESERVED4", 53),
  ("RW", 4, "SHORTS"),                            # Shortcuts for SPIS.
  ("R", 4, "RESERVED5", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED6", 61),
  ("R", 4, "SEMSTAT"),                           # Semaphore status.
  ("R", 4, "RESERVED7", 15),
  ("RW", 4, "STATUS"),                            # Status from last transaction.
  ("R", 4, "RESERVED8", 47),
  ("RW", 4, "ENABLE"),                            # Enable SPIS.
  ("R", 4, "RESERVED9"),
  ("RW", 4, "PSELSCK"),                           # Pin select for SCK.
  ("RW", 4, "PSELMISO"),                          # Pin select for MISO.
  ("RW", 4, "PSELMOSI"),                          # Pin select for MOSI.
  ("RW", 4, "PSELCSN"),                           # Pin select for CSN.
  ("R", 4, "RESERVED10", 7),
  ("RW", 4, "RXDPTR"),                            # RX data pointer.
  ("RW", 4, "MAXRX"),                             # Maximum number of bytes in the receive buffer.
  ("R", 4, "AMOUNTRX"),                          # Number of bytes received in last granted transaction.
  ("R", 4, "RESERVED11"),
  ("RW", 4, "TXDPTR"),                            # TX data pointer.
  ("RW", 4, "MAXTX"),                             # Maximum number of bytes in the transmit buffer.
  ("R", 4, "AMOUNTTX"),                          # Number of bytes transmitted in last granted transaction.
  ("R", 4, "RESERVED12"),
  ("RW", 4, "CONFIG"),                            # Configuration register.
  ("R", 4, "RESERVED13"),
  ("RW", 4, "DEF"),                               # Default character.
  ("R", 4, "RESERVED14", 24),
  ("RW", 4, "ORC"),                               # Over-read character.
  ("R", 4, "RESERVED15", 654),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_SPIS_Type")
]


#==========================================================================
#==========                      SPIM                      ================
# @brief SPI master with easyDMA 1. (SPIM)
#==========================================================================
,
"SPIM" : [
  ("R", 4, "RESERVED0", 4),
  ("W", 4, "TASKS_START"),                       # Start SPI transaction.
  ("W", 4, "TASKS_STOP"),                        # Stop SPI transaction.
  ("R", 4, "RESERVED1"),
  ("W", 4, "TASKS_SUSPEND"),                     # Suspend SPI transaction.
  ("W", 4, "TASKS_RESUME"),                      # Resume SPI transaction.
  ("R", 4, "RESERVED2", 56),
  ("RW", 4, "EVENTS_STOPPED"),                    # SPI transaction has stopped.
  ("R", 4, "RESERVED3", 2),
  ("RW", 4, "EVENTS_ENDRX"),                      # End of RXD buffer reached.
  ("R", 4, "RESERVED4", 3),
  ("RW", 4, "EVENTS_ENDTX"),                      # End of TXD buffer reached.
  ("R", 4, "RESERVED5", 10),
  ("RW", 4, "EVENTS_STARTED"),                    # Transaction started.
  ("R", 4, "RESERVED6", 109),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED7", 125),
  ("RW", 4, "ENABLE"),                            # Enable SPIM.
  ("R", 4, "RESERVED8"),
  # ("SPIM_PSEL_Type", "PSEL"),                              # Pin select configuration.
  ("R", 4, "RESERVED9", 4),
  ("RW", 4, "FREQUENCY"),                         # SPI frequency.
  ("R", 4, "RESERVED10", 3),
  # ("SPIM_RXD_Type", "RXD"),                                # RXD EasyDMA configuration and status.
  ("R", 4, "RESERVED11"),
  # ("SPIM_TXD_Type", "TXD"),                                # TXD EasyDMA configuration and status.
  ("R", 4, "RESERVED12"),
  ("RW", 4, "CONFIG"),                            # Configuration register.
  ("R", 4, "RESERVED13", 26),
  ("RW", 4, "ORC"),                               # Over-read character.
  ("R", 4, "RESERVED14", 654),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_SPIM_Type")
]


#==========================================================================
#==========                     GPIOTE                     ================
# @brief GPIO tasks and events. (GPIOTE)
#==========================================================================
,
"GPIOTE" : [
  ("W", 4, "TASKS_OUT", 4),                      # Tasks asssociated with GPIOTE channels.
  ("R", 4, "RESERVED0", 60),
  ("RW", 4, "EVENTS_IN", 4),                      # Tasks asssociated with GPIOTE channels.
  ("R", 4, "RESERVED1", 27),
  ("RW", 4, "EVENTS_PORT"),                       # Event generated from multiple pins.
  ("R", 4, "RESERVED2", 97),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 129),
  ("RW", 4, "CONFIG", 4),                         # Channel configuration registers.
  ("R", 4, "RESERVED4", 695),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_GPIOTE_Type")
],

# IO Type Qualifier	Type	Description
# __IM	Struct member	Defines 'read only' permissions
# __OM	Struct member	Defines 'write only' permissions
# __IOM	Struct member	Defines 'read / write' permissions
# __I	Scalar variable	Defines 'read only' permissions
# __O	Scalar variable	Defines 'write only' permissions
# __IO	Scalar variable	Defines 'read / write' permissions
#==========================================================================
#==========                       ADC                      ================
# @brief Analog to digital converter. (ADC)
#==========================================================================

"ADC" : [
  ("W", 4, "TASKS_START"),                       #Start an ADC conversion.
  ("W", 4, "TASKS_STOP"),                        #Stop ADC.
  ("R", 4, "RESERVED0", 62),
  ("RW", 4, "EVENTS_END"),                        #ADC conversion complete.
  ("R", 4, "RESERVED1", 128),
  ("RW", 4, "INTENSET"),                          #Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          #Interrupt enable clear register.
  ("R", 4, "RESERVED2", 61),
  ("R", 4, "BUSY"),                              #ADC busy register.
  ("R", 4, "RESERVED3", 63),
  ("RW", 4, "ENABLE"),                            #ADC enable.
  ("RW", 4, "CONFIG"),                            #ADC configuration register.
  ("R", 4, "RESULT"),                            #Result of ADC conversion.
  ("R", 4, "RESERVED4", 700),
  ("RW", 4, "POWER"),                             #Peripheral power control.
  ("NRF_ADC_Type")
],


#==========================================================================
#==========                      TIMER                     ================
# @brief Timer 0. (TIMER)
#==========================================================================

"TIMER" : [
  ("W", 4, "TASKS_START"),                       # Start Timer.
  ("W", 4, "TASKS_STOP"),                        # Stop Timer.
  ("W", 4, "TASKS_COUNT"),                       # Increment Timer (In counter mode).
  ("W", 4, "TASKS_CLEAR"),                       # Clear timer.
  ("W", 4, "TASKS_SHUTDOWN"),                    # Shutdown timer.
  ("R", 4, "RESERVED0", 11),
  ("W", 4, "TASKS_CAPTURE", 4),                  # Capture Timer value to CC[n] registers.
  ("R", 4, "RESERVED1", 60),
  ("RW", 4, "EVENTS_COMPARE", 4),                 # Compare event on CC[n] match.
  ("R", 4, "RESERVED2", 44),
  ("RW", 4, "SHORTS"),                            # Shortcuts for Timer.
  ("R", 4, "RESERVED3", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED4", 126),
  ("RW", 4, "MODE"),                              # Timer Mode selection.
  ("RW", 4, "BITMODE"),                           # Sets timer behaviour.
  ("R", 4, "RESERVED5"),
  ("RW", 4, "PRESCALER"),                         # 4-bit prescaler to source clock frequency (max value 9). Source clock frequency is divided by 2^SCALE.
  ("R", 4, "RESERVED6", 11),
  ("RW", 4, "CC", 4),                             # Capture/compare registers.
  ("R", 4, "RESERVED7", 683),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_TIMER_Type")
]


#==========================================================================
#==========                     RTC                      ================
# @brief Real time counter 0. (RTC)
#==========================================================================
,
"RTC" : [
  ("W", 4, "TASKS_START"),                       # Start RTC Counter.
  ("W", 4, "TASKS_STOP"),                        # Stop RTC Counter.
  ("W", 4, "TASKS_CLEAR"),                       # Clear RTC Counter.
  ("W", 4, "TASKS_TRIGOVRFLW"),                  # Set COUNTER to 0xFFFFFFF0.
  ("R", 4, "RESERVED0", 60),
  ("RW", 4, "EVENTS_TICK"),                       # Event on COUNTER increment.
  ("RW", 4, "EVENTS_OVRFLW"),                     # Event on COUNTER overflow.
  ("R", 4, "RESERVED1", 14),
  ("RW", 4, "EVENTS_COMPARE", 4),                 # Compare event on CC[n] match.
  ("R", 4, "RESERVED2", 109),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 13),
  ("RW", 4, "EVTEN"),                             # Configures event enable routing to PPI for each RTC event.
  ("RW", 4, "EVTENSET"),                          # Enable events routing to PPI. The reading of this register gives the value of EVTEN.
  ("RW", 4, "EVTENCLR"),                          # Disable events routing to PPI. The reading of this register gives the value of EVTEN.
  ("R", 4, "RESERVED4", 110),
  ("R", 4, "COUNTER"),                           # Current COUNTER value.
  ("RW", 4, "PRESCALER"),                         # 12-bit prescaler for COUNTER frequency (32768/(PRESCALER+1)). Must be written when RTC is STOPed.
  ("R", 4, "RESERVED5", 13),
  ("RW", 4, "CC", 4),                             # Capture/compare registers.
  ("R", 4, "RESERVED6", 683),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_RTC_Type")
]


#==========================================================================
#==========                      TEMP                      ================
# @brief Temperature Sensor. (TEMP)
#==========================================================================
,
"TEMP" : [
  ("W", 4, "TASKS_START"),                       # Start temperature measurement.
  ("W", 4, "TASKS_STOP"),                        # Stop temperature measurement.
  ("R", 4, "RESERVED0", 62),
  ("RW", 4, "EVENTS_DATARDY"),                    # Temperature measurement complete, data ready event.
  ("R", 4, "RESERVED1", 128),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED2", 127),
  ("R",  4, "TEMP"),                              # Die temperature in degC, 2's complement format, 0.25 degC pecision.
  ("R", 4, "RESERVED3", 700),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_TEMP_Type")
]


#==========================================================================
#==========                     RNG                      ================
# @brief Random Number Generator. (RNG)
#==========================================================================
,
"RNG" : [
  ("W", 4, "TASKS_START"),                       # Start the random number generator.
  ("W", 4, "TASKS_STOP"),                        # Stop the random number generator.
  ("R", 4, "RESERVED0", 62),
  ("RW", 4, "EVENTS_VALRDY"),                     # New random number generated and written to VALUE register.
  ("R", 4, "RESERVED1", 63),
  ("RW", 4, "SHORTS"),                            # Shortcuts for the RNG.
  ("R", 4, "RESERVED2", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register
  ("R", 4, "RESERVED3", 126),
  ("RW", 4, "CONFIG"),                            # Configuration register.
  ("R", 4, "VALUE"),                             # RNG random number.
  ("R", 4, "RESERVED4", 700),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_RNG_Type")
]


#==========================================================================
#==========                       ECB                      ================
# @brief AES ECB Mode Encryption. (ECB)
#==========================================================================
,
"ECB" : [
  ("W", 4, "TASKS_STARTECB"),                    # Start ECB block encrypt. If a crypto operation is running, this will not initiate a new encryption and the ERRORECB event will  be triggered.
  ("W", 4, "TASKS_STOPECB"),                     # Stop current ECB encryption. If a crypto operation is running, this will will trigger the ERRORECB event.
  ("R", 4, "RESERVED0", 62),
  ("RW", 4, "EVENTS_ENDECB"),                     # ECB block encrypt complete.
  ("RW", 4, "EVENTS_ERRORECB"),                   # ECB block encrypt aborted due to a STOPECB task or due to an error.
  ("R", 4, "RESERVED1", 127),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED2", 126),
  ("RW", 4, "ECBDATAPTR"),                        # ECB block encrypt memory pointer.
  ("R", 4, "RESERVED3", 701),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_ECB_Type")
]


#==========================================================================
#==========                       AAR                      ================
# @brief Accelerated Address Resolver. (AAR)
#==========================================================================
,
"AAR" : [
  ("W", 4, "TASKS_START"),                       # Start resolving addresses based on IRKs specified in the IRK data structure.
  ("R", 4, "RESERVED0"),
  ("W", 4, "TASKS_STOP"),                        # Stop resolving addresses.
  ("R", 4, "RESERVED1", 61),
  ("RW", 4, "EVENTS_END"),                        # Address resolution procedure completed.
  ("RW", 4, "EVENTS_RESOLVED"),                   # Address resolved.
  ("RW", 4, "EVENTS_NOTRESOLVED"),                # Address not resolved.
  ("R", 4, "RESERVED2", 126),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 61),
  ("R", 4, "STATUS"),                            # Resolution status.
  ("R", 4, "RESERVED4", 63),
  ("RW", 4, "ENABLE"),                            # Enable AAR.
  ("RW", 4, "NIRK"),                              # Number of Identity root Keys in the IRK data structure.
  ("RW", 4, "IRKPTR"),                            # Pointer to the IRK data structure.
  ("R", 4, "RESERVED5"),
  ("RW", 4, "ADDRPTR"),                           # Pointer to the resolvable address (6 bytes).
  ("RW", 4, "SCRATCHPTR"),                        # Pointer to a "scratch" data area used for temporary storage during resolution. A minimum of 3 bytes must be reserved.
  ("R", 4, "RESERVED6", 697),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_AAR_Type")
]


#==========================================================================
#==========                       CCM                      ================
# @brief AES CCM Mode Encryption. (CCM)
#==========================================================================
,
"CCM" : [
  ("W", 4, "TASKS_KSGEN"),                       # Start generation of key-stream. This operation will stop by itself when completed.
  ("W", 4, "TASKS_CRYPT"),                       # Start encrypt/decrypt. This operation will stop by itself when completed.
  ("W", 4, "TASKS_STOP"),                        # Stop encrypt/decrypt.
  ("R", 4, "RESERVED0", 61),
  ("RW", 4, "EVENTS_ENDKSGEN"),                   # Keystream generation completed.
  ("RW", 4, "EVENTS_ENDCRYPT"),                   # Encrypt/decrypt completed.
  ("RW", 4, "EVENTS_ERROR"),                      # Error happened.
  ("R", 4, "RESERVED1", 61),
  ("RW", 4, "SHORTS"),                            # Shortcuts for the CCM.
  ("R", 4, "RESERVED2", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 61),
  ("R", 4, "MICSTATUS"),                         # CCM RX MIC check result.
  ("R", 4, "RESERVED4", 63),
  ("RW", 4, "ENABLE"),                            # CCM enable.
  ("RW", 4, "MODE"),                              # Operation mode.
  ("RW", 4, "CNFPTR"),                            # Pointer to a data structure holding AES key and NONCE vector.
  ("RW", 4, "INPTR"),                             # Pointer to the input packet.
  ("RW", 4, "OUTPTR"),                            # Pointer to the output packet.
  ("RW", 4, "SCRATCHPTR"),                        # Pointer to a "scratch" data area used for temporary storage during resolution. A minimum of 43 bytes must be reserved.
  ("R", 4, "RESERVED5", 697),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_CCM_Type")
]


#==========================================================================
#==========                       WDT                      ================
# @brief Watchdog Timer. (WDT)
#==========================================================================
,
"WDT" : [
  ("W", 4, "TASKS_START"),                       # Start the watchdog.
  ("R", 4, "RESERVED0", 63),
  ("RW", 4, "EVENTS_TIMEOUT"),                    # Watchdog timeout.
  ("R", 4, "RESERVED1", 128),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED2", 61),
  ("R", 4, "RUNSTATUS"),                         # Watchdog running status.
  ("R", 4, "REQSTATUS"),                         # Request status.
  ("R", 4, "RESERVED3", 63),
  ("RW", 4, "CRV"),                               # Counter reload value in number of 32kiHz clock cycles.
  ("RW", 4, "RREN"),                              # Reload request enable.
  ("RW", 4, "CONFIG"),                            # Configuration register.
  ("R", 4, "RESERVED4", 60),
  ("W", 4, "RR", 8),                             # Reload requests registers.
  ("R", 4, "RESERVED5", 631),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_WDT_Type")
]


#==========================================================================
#==========                      QDEC                      ================
# @brief Rotary decoder. (QDEC)
#==========================================================================
,
"QDEC" : [
  ("W", 4, "TASKS_START"),                       # Start the quadrature decoder.
  ("W", 4, "TASKS_STOP"),                        # Stop the quadrature decoder.
  ("W", 4, "TASKS_READCLRACC"),                  # Transfers the content from ACC registers to ACCREAD registers, and clears the ACC registers.
  ("R", 4, "RESERVED0", 61),
  ("RW", 4, "EVENTS_SAMPLERDY"),                  # A new sample is written to the sample register.
  ("RW", 4, "EVENTS_REPORTRDY"),                  # REPORTPER number of samples accumulated in ACC register, and ACC register different than zero.
  ("RW", 4, "EVENTS_ACCOF"),                      # ACC or ACCDBL register overflow.
  ("R", 4, "RESERVED1", 61),
  ("RW", 4, "SHORTS"),                            # Shortcuts for the QDEC.
  ("R", 4, "RESERVED2", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 125),
  ("RW", 4, "ENABLE"),                            # Enable the QDEC.
  ("RW", 4, "LEDPOL"),                            # LED output pin polarity.
  ("RW", 4, "SAMPLEPER"),                         # Sample period.
  ("R", 4, "SAMPLE"),                            # Motion sample value.
  ("RW", 4, "REPORTPER"),                         # Number of samples to generate an EVENT_REPORTRDY.
  ("R", 4, "ACC"),                               # Accumulated valid transitions register.
  ("R", 4, "ACCREAD"),                           # Snapshot of ACC register. Value generated by the TASKS_READCLEACC task.
  ("RW", 4, "PSELLED"),                           # Pin select for LED output.
  ("RW", 4, "PSELA"),                             # Pin select for phase A input.
  ("RW", 4, "PSELB"),                             # Pin select for phase B input.
  ("RW", 4, "DBFEN"),                             # Enable debouncer input filters.
  ("R", 4, "RESERVED4", 5),
  ("RW", 4, "LEDPRE"),                            # Time LED is switched ON before the sample.
  ("R", 4, "ACCDBL"),                            # Accumulated double (error) transitions register.
  ("R", 4, "ACCDBLREAD"),                        # Snapshot of ACCDBL register. Value generated by the TASKS_READCLEACC task.
  ("R", 4, "RESERVED5", 684),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_QDEC_Type")
]


#==========================================================================
#==========                     LPCOMP                     ================
# @brief Low power comparator. (LPCOMP)
#==========================================================================
,
"LPCOMP" : [
  ("W", 4, "TASKS_START"),                       # Start the comparator.
  ("W", 4, "TASKS_STOP"),                        # Stop the comparator.
  ("W", 4, "TASKS_SAMPLE"),                      # Sample comparator value.
  ("R", 4, "RESERVED0", 61),
  ("RW", 4, "EVENTS_READY"),                      # LPCOMP is ready and output is valid.
  ("RW", 4, "EVENTS_DOWN"),                       # Input voltage crossed the threshold going down.
  ("RW", 4, "EVENTS_UP"),                         # Input voltage crossed the threshold going up.
  ("RW", 4, "EVENTS_CROSS"),                      # Input voltage crossed the threshold in any direction.
  ("R", 4, "RESERVED1", 60),
  ("RW", 4, "SHORTS"),                            # Shortcuts for the LPCOMP.
  ("R", 4, "RESERVED2", 64),
  ("RW", 4, "INTENSET"),                          # Interrupt enable set register.
  ("RW", 4, "INTENCLR"),                          # Interrupt enable clear register.
  ("R", 4, "RESERVED3", 61),
  ("R", 4, "RESULT"),                            # Result of last compare.
  ("R", 4, "RESERVED4", 63),
  ("RW", 4, "ENABLE"),                            # Enable the LPCOMP.
  ("RW", 4, "PSEL"),                              # Input pin select.
  ("RW", 4, "REFSEL"),                            # Reference select.
  ("RW", 4, "EXTREFSEL"),                         # External reference select.
  ("R", 4, "RESERVED5", 4),
  ("RW", 4, "ANADETECT"),                         # Analog detect configuration.
  ("R", 4, "RESERVED6", 694),
  ("RW", 4, "POWER"),                             # Peripheral power control.
  ("NRF_LPCOMP_Type")
]


#==========================================================================
#==========                       SWI                      ================
# @brief SW Interrupts. (SWI)
#==========================================================================
,
"SWI" : [
  ("R", 4, "UNUSED"),                            # Unused.
  ("NRF_SWI_Type")
]


#==========================================================================
#==========                      NVMC                      ================
# @brief Non Volatile Memory Controller. (NVMC)
#==========================================================================
,
"NVMC" : [
  ("R", 4, "RESERVED0", 256),
  ("R", 4, "READY"),                             # Ready flag.
  ("R", 4, "RESERVED1", 64),
  ("RW", 4, "CONFIG"),                            # Configuration register.

  # union {
  # ("RW", 4, "ERASEPCR1"),                       # Register for erasing a non-protected non-volatile memory page.
  # ("RW", 4, "ERASEPAGE"),                       # Register for erasing a non-protected non-volatile memory page.
  # }"),
  ("RW", 4, "ERASEALL"),                          # Register for erasing all non-volatile user memory.
  ("RW", 4, "ERASEPCR0"),                         # Register for erasing a protected non-volatile memory page.
  ("RW", 4, "ERASEUICR"),                         # Register for start erasing User Information Congfiguration Registers.
  ("NRF_NVMC_Type")
]


#==========================================================================
#==========                       PPI                      ================
# @brief PPI controller. (PPI)
#==========================================================================
,
"PPI" : [
  ("PPI_TASKS_CHG_Type", "TASKS_CHG", 4),                  # Channel group tasks.
  ("R", 4, "RESERVED0", 312),
  ("RW", 4, "CHEN"),                              # Channel enable.
  ("RW", 4, "CHENSET"),                           # Channel enable set.
  ("RW", 4, "CHENCLR"),                           # Channel enable clear.
  ("R", 4, "RESERVED1"),
  # ("PPI_CH_Type CH", 16),                               # PPI Channel.
  ("R", 4, "RESERVED2", 156),
  ("RW", 4, "CHG", 4),                            # Channel group configuration.
  ("NRF_PPI_Type")
]

# typedef struct {
#   __IO uint32_t  EEP;                               /*!< Channel event end-point.                                              */
#   __IO uint32_t  TEP;                               /*!< Channel task end-point.                                               */
# } PPI_CH_Type;



#==========================================================================
#==========                      FICR                      ================
# @brief Factory Information Configuration. (FICR)
#==========================================================================
,
"FICR" : [
  ("R", 4, "RESERVED0", 4),
  ("R", 4, "CODEPAGESIZE"),                      # Code memory page size in bytes.
  ("R", 4, "CODESIZE"),                          # Code memory size in pages.
  ("R", 4, "RESERVED1", 4),
  ("R", 4, "CLENR0"),                            # Length of code region 0 in bytes.
  ("R", 4, "PPFC"),                              # Pre-programmed factory code present.
  ("R", 4, "RESERVED2"),
  ("R", 4, "NUMRAMBLOCK"),                       # Number of individualy controllable RAM blocks.

  # union {
  # ("R", 4, "SIZERAMBLOCK", 4),                 # Deprecated array of size of RAM block in bytes. This name is kept for backward compatinility purposes. Use SIZERAMBLOCKS  instead.
  # ("R", 4, "SIZERAMBLOCKS"),                   # Size of RAM blocks in bytes.
  # }"),
  ("R", 4, "RESERVED3", 5),
  ("R", 4, "CONFIGID"),                          # Configuration identifier.
  ("R", 4, "DEVICEID", 2),                       # Device identifier.
  ("R", 4, "RESERVED4", 6),
  ("R", 4, "ER", 4),                             # Encryption root.
  ("R", 4, "IR", 4),                             # Identity root.
  ("R", 4, "DEVICEADDRTYPE"),                    # Device address type.
  ("R", 4, "DEVICEADDR", 2),                     # Device address.
  ("R", 4, "OVERRIDEEN"),                        # Radio calibration override enable.
  ("R", 4, "NRF_1MBIT", 5),                      # Override values for the OVERRIDEn registers in RADIO for NRF_1Mbit mode.
  ("R", 4, "RESERVED5", 10),
  ("R", 4, "BLE_1MBIT", 5),                      # Override values for the OVERRIDEn registers in RADIO for BLE_1Mbit mode.
  ("NRF_FICR_Type")
]


#==========================================================================
#==========                      UICR                      ================
# @brief User Information Configuration. (UICR)
#==========================================================================
,
"UICR" : [
  ("RW", 4, "CLENR0"),                            # Length of code region 0.
  ("RW", 4, "RBPCONF"),                           # Readback protection configuration.
  ("RW", 4, "XTALFREQ"),                          # Reset value for CLOCK XTALFREQ register.
  ("R", 4, "RESERVED0"),
  ("R", 4, "FWID"),                              # Firmware ID.
  # union {
  # ("RW", 4, "NRFFW", 15),                       # Reserved for Nordic firmware design.
  # ("RW", 4, "BOOTLOADERADDR"),                  # Bootloader start address.
  # }"),
  ("RW", 4, "NRFHW", 12),                         # Reserved for Nordic hardware design.
  ("RW", 4, "CUSTOMER", 32),                      # Reserved for customer.
  ("NRF_UICR_Type")
]


#==========================================================================
#==========                      GPIO                      ================
# @brief General purpose input and output. (GPIO)
#==========================================================================
,
"GPIO" : [
  ("R", 4, "RESERVED0", 321),
  ("RW", 4, "OUT"),                               # Write GPIO port.
  ("RW", 4, "OUTSET"),                            # Set individual bits in GPIO port.
  ("RW", 4, "OUTCLR"),                            # Clear individual bits in GPIO port.
  ("R", 4, "IN"),                                # Read GPIO port.
  ("RW", 4, "DIR"),                               # Direction of GPIO pins.
  ("RW", 4, "DIRSET"),                            # DIR set register.
  ("RW", 4, "DIRCLR"),                            # DIR clear register.
  ("R", 4, "RESERVED1", 120),
  ("RW", 4, "PIN_CNF", 32),                       # Configuration of GPIO pins.
  ("NRF_GPIO_Type")
]
}

#==========================================================================
#==========              Peripheral memory map             ================
#==========================================================================

addr_to_bases = {

  0x40000000 : ["NRF_POWER_BASE", "NRF_CLOCK_BASE", "NRF_MPU_BASE", "NRF_AMLI_BASE"],
  0x40001000 : "NRF_RADIO_BASE",
  0x40002000 : "NRF_UART0_BASE",
  0x40003000 : ["NRF_SPI0_BASE", "NRF_TWI0_BASE"],
  0x40004000 : [ "NRF_SPI1_BASE", "NRF_TWI1_BASE", "NRF_SPIS1_BASE", "NRF_SPIM1_BASE" ],
  0x40006000 : "NRF_GPIOTE_BASE",
  0x40007000 : "NRF_ADC_BASE",
  0x40008000 : "NRF_TIMER0_BASE",
  0x40009000 : "NRF_TIMER1_BASE",
  0x4000A000 : "NRF_TIMER2_BASE",
  0x4000B000 : "NRF_RTC0_BASE",
  0x4000C000 : "NRF_TEMP_BASE",
  0x4000D000 : "NRF_RNG_BASE",
  0x4000E000 : "NRF_ECB_BASE",
  0x4000F000 : [ "NRF_AAR_BASE", "NRF_CCM_BASE" ],
  0x40010000 : "NRF_WDT_BASE",
  0x40011000 : "NRF_RTC1_BASE",
  0x40012000 : "NRF_QDEC_BASE",
  0x40013000 : "NRF_LPCOMP_BASE",
  0x40014000 : "NRF_SWI_BASE",
  0x4001E000 : "NRF_NVMC_BASE",
  0x4001F000 : "NRF_PPI_BASE",
  0x10000000 : "NRF_FICR_BASE",
  0x10001000 : "NRF_UICR_BASE",
  0x50000000 : "NRF_GPIO_BASE",
}
base_to_addr = {
  "NRF_POWER_BASE" : 0x40000000,
  "NRF_CLOCK_BASE" : 0x40000000,
  "NRF_MPU_BASE" : 0x40000000,
  "NRF_AMLI_BASE" : 0x40000000,
  "NRF_RADIO_BASE" : 0x40001000,
  "NRF_UART0_BASE" : 0x40002000,
  "NRF_SPI0_BASE" : 0x40003000,
  "NRF_TWI0_BASE" : 0x40003000,
  "NRF_SPI1_BASE" : 0x40004000,
  "NRF_TWI1_BASE" : 0x40004000,
  "NRF_SPIS1_BASE" : 0x40004000,
  "NRF_SPIM1_BASE" : 0x40004000,
  "NRF_GPIOTE_BASE" : 0x40006000,
  "NRF_ADC_BASE" : 0x40007000,
  "NRF_TIMER0_BASE" : 0x40008000,
  "NRF_TIMER1_BASE" : 0x40009000,
  "NRF_TIMER2_BASE" : 0x4000A000,
  "NRF_RTC0_BASE" : 0x4000B000,
  "NRF_TEMP_BASE" : 0x4000C000,
  "NRF_RNG_BASE" : 0x4000D000,
  "NRF_ECB_BASE" : 0x4000E000,
  "NRF_AAR_BASE" : 0x4000F000,
  "NRF_CCM_BASE" : 0x4000F000,
  "NRF_WDT_BASE" : 0x40010000,
  "NRF_RTC1_BASE" : 0x40011000,
  "NRF_QDEC_BASE" : 0x40012000,
  "NRF_LPCOMP_BASE" : 0x40013000,
  "NRF_SWI_BASE" : 0x40014000,
  "NRF_NVMC_BASE" : 0x4001E000,
  "NRF_PPI_BASE" : 0x4001F000,
  "NRF_FICR_BASE" : 0x10000000,
  "NRF_UICR_BASE" : 0x10001000,
  "NRF_GPIO_BASE" : 0x50000000
}

type_to_base = {
  "NRF_POWER_Type" : "NRF_POWER_BASE",
  "NRF_CLOCK_Type" : "NRF_CLOCK_BASE",
  "NRF_MPU_Type" : "NRF_MPU_BASE",
  "NRF_AMLI_Type" : "NRF_AMLI_BASE",
  "NRF_RADIO_Type" : "NRF_RADIO_BASE",
  "NRF_UART_Type" : "NRF_UART0_BASE",
  "NRF_SPI_Type" : "NRF_SPI0_BASE",
  "NRF_TWI_Type" : "NRF_TWI0_BASE",
  "NRF_SPI_Type" : "NRF_SPI1_BASE",
  "NRF_TWI_Type" : "NRF_TWI1_BASE",
  "NRF_SPIS_Type" : "NRF_SPIS1_BASE",
  "NRF_SPIM_Type" : "NRF_SPIM1_BASE",
  "NRF_GPIOTE_Type" : "NRF_GPIOTE_BASE",
  "NRF_ADC_Type" : "NRF_ADC_BASE",
  "NRF_TIMER_Type" : "NRF_TIMER0_BASE",
  "NRF_TIMER_Type" : "NRF_TIMER1_BASE",
  "NRF_TIMER_Type" : "NRF_TIMER2_BASE",
  "NRF_RTC_Type" : "NRF_RTC0_BASE",
  "NRF_TEMP_Type" : "NRF_TEMP_BASE",
  "NRF_RNG_Type" : "NRF_RNG_BASE",
  "NRF_ECB_Type" : "NRF_ECB_BASE",
  "NRF_AAR_Type" : "NRF_AAR_BASE",
  "NRF_CCM_Type" : "NRF_CCM_BASE",
  "NRF_WDT_Type" : "NRF_WDT_BASE",
  "NRF_RTC_Type" : "NRF_RTC1_BASE",
  "NRF_QDEC_Type" : "NRF_QDEC_BASE",
  "NRF_LPCOMP_Type" : "NRF_LPCOMP_BASE",
  "NRF_SWI_Type" : "NRF_SWI_BASE",
  "NRF_NVMC_Type" : "NRF_NVMC_BASE",
  "NRF_PPI_Type" : "NRF_PPI_BASE",
  "NRF_FICR_Type" : "NRF_FICR_BASE",
  "NRF_UICR_Type" : "NRF_UICR_BASE",
  "NRF_GPIO_Type" : "NRF_GPIO_BASE",
}
#  ('R', 4, 'RESERVED0', 312)



if __name__ == "__main__":
  for k, v in register_blocks.items():
    print(k, "=>")
    type_str = v.pop()
    base_str = type_to_base[type_str]
    addr_base = base_to_addr[base_str]
    print(type_str, "at", hex(addr_base))
    res_tally = 0

    for idx, item in enumerate(v):
      reg_str = ""
      res_count = 0
      begin_offset  =  (idx+res_tally) * 4
      item_address = begin_offset+addr_base
      if len(item) is 4:
        res_count = item[-1]
        res_tally += (res_count-1)
        item = item[:-1]
      rw, width, name = item
      if res_count >0:
        name+="(%d)"%res_count
        end_addr =  (idx+(res_tally)) * 4

        reg_str = "\t[%s](%s-%s) ~> %s [%s] "%(hex(item_address), hex(begin_offset), hex(end_addr), name, rw)
      else:
        reg_str = "\t[%s](%s) ~> %s [%s]"%(hex(item_address), hex(begin_offset), name, rw)

      #   reg_str = "\t[%s] ~> %s [%s] "%(hex(item_address), hex(begin_offset), hex(end_addr), name, rw)
      # else:
      #   reg_str = "\t[%s] ~> %s [%s]"%(hex(item_address), hex(begin_offset), name, rw)
      print(reg_str)

    print("*"*50)
    print()