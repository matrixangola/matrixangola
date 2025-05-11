[app]
title = UsuarioApp
package.name = usuarioapp
package.domain = org.hamirstudios
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db,txt
version = 1.0
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 23b
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1