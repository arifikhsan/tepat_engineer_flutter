#!/bin/bash

import os

print('refreshing')

# update gradle dependencies
os.chdir('android')
os.system('gradlew --refresh-dependencies')
os.chdir('..')

# get packages
os.system('flutter clean')
os.system('flutter pub get')

# build apk
os.system('flutter packages pub run build_runner clean')
os.system('flutter packages pub run build_runner build --delete-conflicting-outputs')
os.system('flutter build apk --debug --flavor development --target lib/main_development.dart')
# os.system('flutter build apk --release --flavor production --target lib/main_production.dart --target-platform android-arm64 --analyze-size')

print('refreshed')
