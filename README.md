# Clock

This is a time tracking CLI that records your hours into a file.

**Why use clock?** Because using a flashy web or desktop app is distracting, and might not work without internet!

## Setup
 - with git:
```
cd /some/dir
git clone https://github.com/Macuyler/clock.git
# Add PATH="PATH:/some/dir/clock" to your profile/rc file.
```
 - with [mac](https://github.com/Macuyler/mac):
```
mac install https://github.com/Macuyler/clock.git
```

----------

## About
### Clock Logs:
```
Week 2:
  01/05/20: 0:00HR
  01/06/20: 3:53HR
  01/07/20: 4:45HR
  01/08/20: 1:42HR
  01/09/20: 3:49HR
  01/10/20: 2:21HR
  01/11/20: 1:22HR

  Total = 17:52HR
```
Clock will take care of logging how many hours you work each day, and giving you a weekly total. It will automatically take care of formatting each new week, so all you have to do is copy and paste into your invoice.

### Clock Config:
The config file is located at `~/.clock.conf`. This file is simply used to definine a custom file location for your clock log.

*Example:*
```
/home/user/Documents/work/hours.txt
```