[app]
title = Translator3in1
package.name = translator3in1
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,deep-translator,requests,urllib3,chardet,certifi,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.arch = arm64-v8a
android.accept_sdk_license = True

[buildozer]
profile = android
log_level = 2
warn_on_root = 1