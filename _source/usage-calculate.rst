.. raw:: html

    <div align="right"><b>TH</b> | <a href="https://docs.netpie.io/en/usage-calculate.html">EN</a></div>

Service Usage Calculation
==========================

การคำนวณปริมาณการใช้งาน Service ต่างๆ ของ |platform_name| Platform ดูปริมาณการใช้งานในแต่ละรอบบิลได้จาก Web Portal โดยคลิกที่ชื่อผู้ใช้มุมบนขวามือ และเลือกเมนู "Billing" จะถูกแยกการคิดได้เป็นประเภทใหญ่ๆ ดังต่อนี้

.. _api-quota:

API Call
--------------------

ปริมาณการใช้บริการ REST API ทั้งหมดใน |platform_name| Platform มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ


API Request 
	: จำนวนการ Request ผ่าน REST APT โดยดูจากขนาดของ Payload ที่ส่งไป แต่ละ Block มีขนาดไม่เกิน 4 kilobytes


API Response 
	: จำนวนการ Response ผ่าน REST APT โดยดูจากขนาดของ Payload ที่ตอบกลับ แต่ละ Block มีขนาดไม่เกิน 4 kilobytes


.. admonition:: ตัวอย่าง

	การอ่านข้อมูลจาก Time Series Database ผ่าน REST API 1 ครั้ง ข้อมูลที่ส่งไปตอน Request มีขนาด 71 bytes และข้อมูล Response กลับมามีขนาด 10 kilobytes ดังนั้น การนับในครั้งนี้จะเป็นดังนี้ 

	
	Request ส่ง Payload ไป ขนาด 71 bytes	= 71 / 1024*4 = 1 Operation(Request) เศษที่หาร 4KB ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block

	
	Response ตอบกลับ Payload ขนาด 10KB  	= 10 / 4 = 3 Operations(Response) เศษที่หาร 4KB ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block

	
	รวม API Call Quota ที่ถูกใช้ไป 		= 1 + 3 = 4 Operations

|

Device Online 
--------------------

ระยะเวลารวมทั้งหมดที่ Device เชื่อมต่ออยู่ใน |platform_name| Platform มีหน่วยนับเป็นวินาที(Second)

.. admonition:: ตัวอย่าง

	มี Device ที่ลงทะเบียนใช้งาน |platform_name| Platform อยู่ 2 Devices Device เพื่อส่งข้อมูลสถานะการทำงานต่างๆ ของเครื่องจักรไปเก็บที่ Platform โดย Device1 เชื่อมต่อ Platform เวลา 08:00:03 ส่งข้อมูลเสร็จและตัดการเชื่อมต่อ Platform ที่เวลา 08:00:15 ส่วน Device2 เชื่อมต่อ Platform เวลา 08:00:05 ส่งข้อมูลเสร็จและตัดการเชื่อมต่อ Platform ที่เวลา 08:00:20 ดังนั้น เวลารวมในกรณีนี้จะเป็น


	Device1 Online (08:00:03 - 08:00:15)	 = 12 วินาที


	Device2 Online (08:00:05 - 08:00:20)	 = 15 วินาที 


	รวม Connection Quota ที่ถูกใช้ไป 			 = 12 + 15 = 27 วินาที

|

.. _message-quota:

Real Time Message
----------------------------

ปริมาณการใช้บริการที่เกี่ยวกับ MQTT มีหน่วยนับเป็น Message โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ


MQTT Publish
	: จำนวน Message ที่ Publish โดยดูจากขนาดของ Message แต่ละ Block มีขนาดไม่เกิน 4 kilobytes


MQTT Subscribe
	: จำนวนครั้งในการขอ Subscribe แต่ละครั้งนับเป็น 1 Message


MQTT Deliver
	: จำนวน Message ที่ส่งให้ Device ที่ขอ Subscribe ไว้ โดยดูจากขนาดของ Message แต่ละ Block มีขนาดไม่เกิน 4 kilobytes


MQTT Connect
	: จำนวนครั้งในการขอเชื่อมต่อ (Connect) มายัง |platform_name| Platform แต่ละครั้งนับเป็น 1 Message


.. admonition:: ตัวอย่าง

	มี 5 Devices เชื่อมต่อมายัง |platform_name| Platform โดย Device1 Publish Message ขนาด 6 kilobytes ไปที่ myDevice Topic ซึ่ง Device2, Device3, Device4 และ Device5 ได้ทำการ Subscribe ที่ myDevice Topic อยู่ ดังนั้น การนับในครั้งนี้จะเป็นดังนี้
	

	5 Devices เชื่อมต่อ |platform_name| Platform		 = 5 x 1 = 5 Messages(MQTT Connect)
	

	Device1 Publish Message ขนาด 6 KB 		 = 6 / 4 = 2 Messages(MQTT Publish) เศษที่หาร 4 ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block
	

	Device2-5 (4 Devices) ขอ Subscribe Topic = 4 x 1 = 4 Messages(MQTT Subscribe)
	

	Device2-5 (4 Devices) ได้รับ Message 		 = 4 x 2 = 8 Messages(MQTT Deliver) จากการ Subscribe ได้ Message ที่ Device1 Publish ขนาด 6 KB
	

	รวม Message Quota ที่ถูกใช้ไป 			 = 5 + 2 + 4 + 8 = 19 Messages

|

.. _shadow-quota:

Shadow Read/Write
--------------------

ปริมาณการใช้บริการที่เกี่ยวกับ Shadow มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ


Shadow Read
	: จำนวนการอ่าน Shadow โดยดูจากขนาดของ Shadow ที่ถูกอ่านออกมา แต่ละ Block มีขนาดไม่เกิน 1 kilobyte


Shadow Write
	: จำนวนการเขียน Shadow โดยดูจากขนาดของ Shadow ที่ส่งไปเขียน แต่ละ Block มีขนาดไม่เกิน 1 kilobyte


Shadow Expression
	: จำนวนครั้งที่ Shadow มีการรัน Expression จะอยู่ในส่วนของการแปลงข้อมูล (Data Transformation)


.. admonition:: ตัวอย่าง

	Device 1 ตัว เมื่อ online ขึ้นมาจะทำการอ่าน Shadow ทั้งหมดของตนเอง (ขนาด Shadow 2 kilobytes) มาเป็นค่าเริ่มต้นสำหรับการตั้งค่าการทำงาน หลังจากนั้น Device จะส่งค่าอุณหภูมิปัจจุบันของตัวเองไปอัพเดทที่ Shadow (ขนาดข้อมูลที่ส่งไป 20 bytes) โดยค่าที่ส่งไปมีหน่วยเป็นฟาเรนไฮต์ ซึ่งมีการกำหนด Expression สำหรับแปลงหน่วยเป็นเซลเซียส คำนวนปริมาณ Shadow Operation Quota ที่ถูกใช้ไปได้ดังนี้
	

	2 Operations(Shadow Read) + 1 Operation(Shadow Write) + 1 Operation(Shadow Expression) = 4 Operations

|

.. _time-series-quota:

Time Series Data Store
-----------------------

ปริมาณข้อมูล (Time Series Data) และระยะเวลาที่ต้องการเก็บข้อมูล มีหน่วยนับเป็น Point-Day หมายความว่า ข้อมูลที่ส่งมาเก็บ 1 จุดข้อมูล (ขนาดข้อมูลไม่เกิน 1 kilobyte) ระยะเวลาในการเก็บ (TTL) 30 วัน ถูกนับเป็น 1 Point-Month หรือ 30 Point-Day 


.. admonition:: ตัวอย่าง

	Device สำหรับวัดความชื้นและอุณหภูมิ(2 data point), วัดค่าและส่งข้อมูลไปเก็บทุก 1 ชั่วโมง(24 time/day), เก็บค่าย้อนหลัง 30 วัน(TTL), ระยะเวลาใช้บริการ 31 วัน คำนวนปริมาณ Quota ที่ถูกใช้ไปได้ดังนี้


	2(data point) x 30(TTL) X 24(time/day) x 31(day) = 44,640 Point-Day หรือเท่ากับ


	44,640 Point-Day / 30 = 1,488 Point-Month

|

.. _trigger-quota:

Trigger & Action
--------------------


ปริมาณการใช้บริการที่เกี่ยวกับ Trigger มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ


Device Trigger
	: Trigger ที่เกิดจาก Device เปลี่ยนสถานะการเชื่อมต่อ Platform จากเชื่อมต่อ (Online) เป็นไม่เชื่อมต่อ (Offline) หรือ จากไม่เชื่อมต่อ (Offline) เป็นเชื่อมต่อ (Online) เซ็ต Trigger Event เป็น ``DEVICE.STATUSCHANGED`` ดูรายละเอียดเพิ่มเติมจาก :ref:`trigger-and-action` ถ้ามีการตั้งค่า Trigger นี้ไว้ ทุกครั้งที่มีการเปลี่ยนสถานะจะถูกนับเป็น 1 Operation / 1 Trigger Event ที่เซ็ตไว้


Shadow Trigger
	: Trigger ที่เกิดจาก Shadow มีการเปลี่ยนแปลงและมีการเซ็ตเงื่อนไขสำหรับตรวจสอบการเปลี่ยนไว้ด้วย เซ็ต Trigger Event เป็น ``SHADOW.UPDATED`` ดูรายละเอียดเพิ่มเติมจาก :ref:`trigger-and-action` ถ้ามีการตั้งค่า Trigger นี้ไว้ ทุกครั้งที่ Shadow มีการเปลี่ยนแปลงและเงื่อนไขเป็นจริง (Trigger Condition ได้ค่าเป็น True) จะถูกนับเป็น 1 Operation / 1 Trigger Condition


.. admonition:: ตัวอย่าง

	จากตัวอย่างการตั้งค่า Trigger ด้านล่าง จะมีทั้งทั้งหมด 3 Triggers (Device Trigger 2 และ Shadow Trigger 1) ถ้ามี 1 Device เชื่อมต่อมายัง Platform และส่งค่าอุณหภูมิ (temp) เข้ามา 3 ครั้ง แต่ละครั้งห่างกันประมาณ 1 นาที ค่าที่ส่งไปเป็น 1, 0 , -1 ตามลำดับ โดยเริ่มต้นอุณหภูมิใน Shadow เป็น 0 เมื่อส่งครบ 3 ครั้ง Device จะตัดการเชื่อมต่อจาก Platform คำนวนปริมาณ Trigger & Action ที่ถูกใช้ไปได้ดังนี้


	Device Online ทำ action ``LINENOTIFY`` และ ``myApp`` = 2 Operations


	ส่งอุณหภูมิ (temp) ครั้งที่ 1 ค่าเป็น 1 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น True = 1 Operations


	ส่งอุณหภูมิ (temp) ครั้งที่ 2 ค่าเป็น 0 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น False = 0 Operations


	ส่งอุณหภูมิ (temp) ครั้งที่ 3 ค่าเป็น -1 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น False = 0 Operations


	Device Offline (``DEVICE.STATECHANGED``) ทำ action ``LINENOTIFY`` และ ``myApp`` = 2 Operations


	รวม Trigger & Action Quota ที่ถูกใช้ไป 			 = 2 + 1 + 0 + 0 + 2 = 5 Operations
	
.. code-block:: json

	{
		"enabled": true,
		"trigger": [{
			"action": "LINENOTIFY",
			"event": "DEVICE.STATECHANGED",
			"msg": "My Device {{$NEW.statustext}}, statuscode: {{$NEW.status}}",
			"option": {
				"url": "https://notify-api.line.me/api/notify",
				"linetoken": "HBfiJA309FWFouCPzK5WhGUvJT1RvN3xb6hGxnIqAAA"
			}
		},
		{
			"action": "myApp",
			"event": "DEVICE.STATECHANGED",
			"msg": "{{$NEW.statustext}}",
			"option": {
				"deviceid": "155941ce-1f4a-4e57-1864-1759af4f872c"
			}
		},
		{
			"action": "checkTemp",
			"event": "SHADOW.UPDATED",
			"condition": "$NEW.bedroom.temp > 0",
			"msg": "My temperature was change from {{$PREV.bedroom.temp}} to {{$NEW.bedroom.temp}}",
			"option": {
				"url": "https://mywebhook/devicetemp"
			}
		}]
	}

|

.. _datasource-quota:

Datasource
--------------------

ปริมาณขนาดข้อมูลสะสม (หน่วยเป็น Byte) ที่เกิดจากการ Download ข้อมูลจาก Time-series data storage หรือก็คือ Data Transfer ซึ่งการดึงข้อมูลทั้งจากระบบภายนอก หรือ Dashboard ที่มีให้ใช้งานภายในจะถูกคิดโควต้าส่วนนี้ทั้งหมด

.. admonition:: ตัวอย่าง
	
	มีการเก็บข้อมูลอุณหภุมิและความชื้นลงใน Time-series data storage มีการพัฒนา Web Application เพื่อมาดึงข้อมูลจาก Time-series data storage ไปแสดงผลเป็นกราฟ โดยความถี่ในการดึงข้อมูลมาอัพเดทในกราฟ คือ ทุก 5 นาที (Auto Refresh), ขนาดข้อมูลที่ดึงไปแสดงผลในแต่ละครั้ง คือ 2.5 KB ดังนั้น ถ้ามีการเปิด Web Application ให้แสดงผลกราฟทิ้งไว้นาน 1 ชั่วโมง จะคำนวณปริมาณ Datasource ที่ถูกใช้ไปได้ ดังนี้


	Datasource = 60(นาที) / 5(นาที) x 2.5(KB) = 30 KB 

	
	คิดเป็นหน่วย Byte = 30 * 1024 = 30,720 B