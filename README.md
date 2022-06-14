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
adb push <file> <android-folder>
adb pull <android-file-path>

3. write down android path for tip

# app storage path
/data/user/0/org.kivy.writetest/files/<file>
# primary external storage path
/storage/emulated/0/<file> 
