# Clock

This is a work timing script for tracking hours.


## Setup

### D-Bus

Clock uses [dbus-python](https://pypi.org/project/dbus-python/), which requires you have [dbus](https://www.freedesktop.org/wiki/Software/dbus/) installed.

#### Install dbus

Debian:

```
apt install dbus
```

Fedora:

```
dnf install dbus
```

macOS:

```
brew install dbus
```

### General

Clone the repo and install the requirements.

```
git clone https://github.com/macuyler/clock.git
cd clock
python3 -m pip install --user requirements.txt
```

> Checkout [gitbin](https://github.com/macuyler/gitbin) for quickly adding scripts to your path.


## Configuration

The clock configuration is located in the `~/.config/clock/clock.conf` file.
You can setup work profiles there with the following format:

```
profile_name:/absolute/path/to/log-file.txt
```

> Note: The log file must exist prior to using the profile.

### Notifications

You can also set up timed notifications in the config file.
These can be a reminder to take a break, or that you are still clocked in.
You can set the notification interval with the following format:

```
_notify_me:60.0
```

> Where `60.0` is the number of minutes in-between notifications.


## Usage

Running the clock script will start an infinite loop that prompts you for input.
The idea is that you can run the script and then minimize the window or something.

```
$ clock [-h] [-n NOTIFY_ME] [profile]
┏━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ You are clocked in!     ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Enter [t] to show time. ┃
┃ Enter [q] to quit.      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━┛
 >
```

You have to option to pass in the name of a profile that you want to use.
If you don't specify a profile, it will attempt to find a profile named **default**.

```
clock school
```

Incase of an invalid config file or profile,
clock will print the number of hours you just clocked to _stdout_.
All other clock output including _UI_ elements are printed over _stderr_.
This will allow you to redirect _stdout_ to a log file if needed.

```
clock > log.txt
```

You can also set a temporary notification interval using the `--notify-me` flag.

```
clock --notify-me 15
```
