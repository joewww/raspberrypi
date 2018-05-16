# BlueLED
Flask, GPIO, LED fun

## Usage

*root is needed for GPIO access, and port 80*

run:

`
sudo python blue-api.py
`

toggle led:

`curl localhost`

blink mode:

`curl localhost/blink`

## Useful Commands
Show GPIO pin layout:

`
$ pinout
`

## Dependencies

- Hardware:
  - Raspberry Pi 3
  - 1 Blue LED
- Software:
  - Raspbian 9 (stretch)
  - RPi.GPIO (0.6.3)
  - Flask (0.12.1)


