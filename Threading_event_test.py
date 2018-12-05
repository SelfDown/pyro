#!/usr/bin/env python
# -*- coding: utf_8 -
import threading
def do(event):
	print "start"
	event.wait()
	print "execute"


if __name__ == '__main__':
	event_obj = threading.Event()
	for i in range(5):
		t = threading.Thread(target=do,args=(event_obj,))
		t.start()
	event_obj.clear()
	while True:
		input_data = raw_input("true/false:")
		print input_data.lower()
		if input_data.lower() == "true":
			event_obj.set()
			break