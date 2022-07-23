
## Planned Features
- USB C
- Rotary Encoders
- SK6812 Neopixel Support
- 32bit controller (ie. STM32)

## Future Planned Features
- BLE
- Multi-USB Support
- OLED Display


## Inception
- Inspiration layout: TM680
![](/HDK/SCO68R/docs/resources/SCO68R-Layout.svg)

- Selected MCU: STM32F103C8T6
    - MCU has 4 timers with STM's "Encoder Mode", SCO68R can support up to 4 rotary encoders.
![SCO68R Pin Config](/HDK/SCO68R/docs/resources/SCO68R-pin-config.png)

## Obstacles
- Neopixel (WS2812 & SK6812) runs on 5v logic whereas STM32 runs on 3.3v logic. 
    - Transistor level shifter circuit is added [(Level Shifter Circuit)](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all)
    - ![](/HDK/SCO68R/docs/resources/level-shifter-circuit.png)

## BOM

@@include[bom.md](includes/my-file.md)
