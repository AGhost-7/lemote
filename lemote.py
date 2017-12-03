#!/usr/bin/env python3

import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import cwiid

print('Connecting to wiimote...')
remote = cwiid.Wiimote()
remote.rpt_mode = cwiid.RPT_ACC
remote.led = 1
print('Connected')

def on_draw(wid, context):
    (x, y, z) = remote.state['acc']
    print('on_draw (x, y, z):', x, y, z)
    context.set_source_rgb(0, 0, 0)
    context.move_to(100, 100)
    context.line_to(x, y)
    context.stroke()

window = Gtk.Window(title='this is a title')
area = Gtk.DrawingArea()
area.connect("draw", on_draw)
window.add(area)
window.resize(500, 500)
window.set_position(Gtk.WindowPosition.CENTER)
window.connect("delete-event", Gtk.main_quit)
window.show_all()

def on_tick():
    area.queue_draw()
    return True

GLib.timeout_add(50, on_tick)
Gtk.main()

print('ok bye')
