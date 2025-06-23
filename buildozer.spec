
[app]
title = برنامج مطابقة الأسماء والأقسام
package.name = name_matcher
version = 1.0.0
source.dir = .
source.include_exts = py,png,jpg,kv,xlsx
source.include_patterns = assets/*, images/*
requirements = python3,kivy,pandas,openpyxl,rapidfuzz
android.permissions = INTERNET,ACCESS_FINE_LOCATION

[android]
android.api = 30
android.arch = armeabi-v7a
android.sdk = 20
android.ndk = 19b
android.private_storage = True
