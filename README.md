# Empire Era

git clone ssh://git@github.com/tiedwu/empire-era
git checkout v1.0

# git push remote
git push origin v1.0:v1.0

# debug method
1. adb logcat -s python
2. adb logcat -s Empire

# Known Issues
1. press over 1 seconds
2. soldiers is negative even attackiing successful (fixed)

# adb push/pull
adb push <file> <android-path>
adb pull <android-file-path>
