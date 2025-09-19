#!/bin/bash

if [ "$1" = "off" ]; then
    echo "Disabling Mouse Keys and restoring defaults..."
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-enable false
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-max-speed 10
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-accel-time 300

elif [ "$1" = "status" ]; then
    echo "📊 Mouse Keys status:"
else
    echo "Enabling Mouse Keys with faster settings..."
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-enable true
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-max-speed 100
    gsettings set org.gnome.desktop.a11y.keyboard mousekeys-accel-time 100
fi

echo
echo "✅ Current settings:"
echo "mousekeys-enable:    $(gsettings get org.gnome.desktop.a11y.keyboard mousekeys-enable)"
echo "mousekeys-max-speed: $(gsettings get org.gnome.desktop.a11y.keyboard mousekeys-max-speed)"
echo "mousekeys-accel-time:$(gsettings get org.gnome.desktop.a11y.keyboard mousekeys-accel-time)"
