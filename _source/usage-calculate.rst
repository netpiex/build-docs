Service Usage Calculation
==========================

|

การคำนวณปริมาณการใช้งาน Service ต่างๆ ของ |platform_name| Platform จะถูกแยกการคิดได้เป็นประเภทใหญ่ๆ ดังต่อนี้

|

API Call
--------------------

ปริมาณการใช้บริการ REST API ทั้งหมดใน |platform_name| Platform มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ

|

API Request 
	: จำนวนการ Request ผ่าน REST APT โดยดูจากขนาดของ Payload ที่ส่งไป แต่ละ Block มีขนาดไม่เกิน 4 kilobytes

|

API Response 
	: จำนวนการ Response ผ่าน REST APT โดยดูจากขนาดของ Payload ที่ตอบกลับ แต่ละ Block มีขนาดไม่เกิน 4 kilobytes

|

*ตัวอย่าง*
````````````
	การอ่านข้อมูลจาก Time Series Database ผ่าน REST API 1 ครั้ง ข้อมูลที่ส่งไปตอน Request มีขนาด 71 bytes และข้อมูล Response กลับมามีขนาด 10 kilobytes ดังนั้น การนับในครั้งนี้จะเป็นดังนี้ 

	|

	Request ส่ง Payload ไป ขนาด 71 bytes	= 71 / 1024*4 = 1 Operation(Request) เศษที่หาร 4KB ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block

	|

	Response ตอบกลับ Payload ขนาด 10KB  	= 10 / 4 = 3 Operations(Response) เศษที่หาร 4KB ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block

	|

	รวม API Call Quota ที่ถูกใช้ไป 		= 1 + 3 = 4 Operations

|

Real-time Messages
----------------------------

ปริมาณการใช้บริการที่เกี่ยวกับ MQTT มีหน่วยนับเป็น Message โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ

|

MQTT Publish
	: จำนวน Message ที่ Publish โดยดูจากขนาดของ Message แต่ละ Block มีขนาดไม่เกิน 4 kilobytes

|

MQTT Subscribe
	: จำนวนครั้งในการขอ Subscribe แต่ละครั้งนับเป็น 1 Message

|

MQTT Deliver
	: จำนวน Message ที่ส่งให้ Device ที่ขอ Subscribe ไว้ โดยดูจากขนาดของ Message แต่ละ Block มีขนาดไม่เกิน 4 kilobytes

|

MQTT Connect
	: จำนวนครั้งในการขอเชื่อมต่อ (Connect) มายัง |platform_name| Platform แต่ละครั้งนับเป็น 1 Message

|

*ตัวอย่าง*
````````````
	มี 5 Devices เชื่อมต่อมายัง |platform_name| Platform โดย Device1 Publish Message ขนาด 6 kilobytes ไปที่ myDevice Topic ซึ่ง Device2, Device3, Device4 และ Device5 ได้ทำการ Subscribe ที่ myDevice Topic อยู่ ดังนั้น การนับในครั้งนี้จะเป็นดังนี้
	
	|

	5 Devices เชื่อมต่อ |platform_name| Platform		 = 5 x 1 = 5 Messages(MQTT Connect)
	
	|

	Device1 Publish Message ขนาด 6 KB 		 = 6 / 4 = 2 Messages(MQTT Publish) เศษที่หาร 4 ไม่ลงตัวต้องปัดขึ้นเป็นอีก 1 Block
	
	|

	Device2-5 (4 Devices) ขอ Subscribe Topic = 4 x 1 = 4 Messages(MQTT Subscribe)
	
	|

	Device2-5 (4 Devices) ได้รับ Message 		 = 4 x 2 = 8 Messages(MQTT Deliver) จากการ Subscribe ได้ Message ที่ Device1 Publish ขนาด 6 KB
	
	|

	รวม Message Quota ที่ถูกใช้ไป 			 = 5 + 2 + 4 + 8 = 19 Messages

|

Shadow Read/Write
--------------------

ปริมาณการใช้บริการที่เกี่ยวกับ Shadow มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ

|

Shadow Read
	: จำนวนการอ่าน Shadow โดยดูจากขนาดของ Shadow ที่ถูกอ่านออกมา แต่ละ Block มีขนาดไม่เกิน 1 kilobyte

|

Shadow Write
	: จำนวนการเขียน Shadow โดยดูจากขนาดของ Shadow ที่ส่งไปเขียน แต่ละ Block มีขนาดไม่เกิน 1 kilobyte

|

Shadow Expression
	: จำนวนครั้งที่ Shadow มีการรัน Expression จะอยู่ในส่วนของการแปลงข้อมูล (Data Transformation)

|

*ตัวอย่าง*
````````````
	Device 1 ตัว เมื่อ online ขึ้นมาจะทำการอ่าน Shadow ทั้งหมดของตนเอง (ขนาด Shadow 2 kilobytes) มาเป็นค่าเริ่มต้นสำหรับการตั้งค่าการทำงาน หลังจากนั้น Device จะส่งค่าอุณหภูมิปัจจุบันของตัวเองไปอัพเดทที่ Shadow (ขนาดข้อมูลที่ส่งไป 20 bytes) โดยค่าที่ส่งไปมีหน่วยเป็นฟาเรนไฮต์ ซึ่งมีการกำหนด Expression สำหรับแปลงหน่วยเป็นเซลเซียส คำนวนปริมาณ Shadow Operation Quota ที่ถูกใช้ไปได้ดังนี้

	|

	2 Operations(Shadow Read) + 1 Operation(Shadow Write) + 1 Operation(Shadow Expression) = 4 Operations

Time Series Data Store
-----------------------

ปริมาณข้อมูล (Time Series Data) และระยะเวลาที่ต้องการเก็บข้อมูล มีหน่วยนับเป็น Point-Day, Point-Month หรือ Point-Year หมายความว่า ข้อมูลที่ส่งมาเก็บ 1 จุดข้อมูล (ขนาดข้อมูลไม่เกิน 1 kilobyte) ระยะเวลาในการเก็บ (TTL) 1 วัน, 1 เดือน หรือ 1 ปี ถูกนับเป็น 1 Point-Day, 1 Point-Month หรือ 1 Point-Year ตามลำดับ จำนวนจุดข้อมูลที่เก็บได้จะแปรผกผันกับระยะเวลาในการเก็บ (ถ้าเก็บนานจำนวนจุดข้อมูลที่เก็บได้จะน้อยลง)

|

*ตัวอย่าง*
````````````
	Device สำหรับวัดความชื้นและอุณหภูมิ วัดค่าและส่งข้อมูลไปเก็บทุก 1 ชั่วโมง เก็บค่าย้อนหลัง 7 วัน ภายในระยะเวลา 30 วัน คำนวนปริมาณ Store Quota ที่ถูกใช้ไปได้ดังนี้

	|

	2(point data) x [ 24(hours/day) x 30(days) ] x 7(days) = 10080 Point-Day

	|

	หรือ

	|

	2(point data) x [ 24(hours/day) x 30(days) ] x [ 7(days) / 30(days/month) ] = 336 Point-Month

	|	

	หรือ

	|

	2(point data) x [ 24(hours/day) x 30(days) ] x [ 7(days) / 365(days/year) ] = 27.62 Point-Year

|

Trigger & Action
--------------------

|

ปริมาณการใช้บริการที่เกี่ยวกับ Trigger มีหน่วยนับเป็น Operation โดยการกระทำที่จะถูกนับเป็นการใช้งานประเภทนี้ คือ

|

Device Trigger
	: Trigger ที่เกิดจาก Device เปลี่ยนสถานะการเชื่อมต่อ Platform จากเชื่อมต่อ (Online) เป็นไม่เชื่อมต่อ (Offline) หรือ จากไม่เชื่อมต่อ (Offline) เป็นเชื่อมต่อ (Online) เซ็ต Trigger Event เป็น ``DEVICE.STATUSCHANGED`` ดูรายละเอียดเพิ่มเติมจาก :ref:`trigger-and-action` ถ้ามีการตั้งค่า Trigger นี้ไว้ ทุกครั้งที่มีการเปลี่ยนสถานะจะถูกนับเป็น 1 Operation / 1 Trigger Event ที่เซ็ตไว้

|

Shadow Trigger
	: Trigger ที่เกิดจาก Shadow มีการเปลี่ยนแปลงและมีการเซ็ตเงื่อนไขสำหรับตรวจสอบการเปลี่ยนไว้ด้วย เซ็ต Trigger Event เป็น ``SHADOW.UPDATED`` ดูรายละเอียดเพิ่มเติมจาก :ref:`trigger-and-action` ถ้ามีการตั้งค่า Trigger นี้ไว้ ทุกครั้งที่ Shadow มีการเปลี่ยนแปลงและเงื่อนไขเป็นจริง (Trigger Condition ได้ค่าเป็น True) จะถูกนับเป็น 1 Operation / 1 Trigger Condition

|

*ตัวอย่าง*
````````````
	จากตัวอย่างการตั้งค่า Trigger ด้านล่าง จะมีทั้งทั้งหมด 3 Triggers (Device Trigger 2 และ Shadow Trigger 1) ถ้ามี 1 Device เชื่อมต่อมายัง Platform และส่งค่าอุณหภูมิ (temp) เข้ามา 3 ครั้ง แต่ละครั้งห่างกันประมาณ 1 นาที ค่าที่ส่งไปเป็น 1, 0 , -1 ตามลำดับ โดยเริ่มต้นอุณหภูมิใน Shadow เป็น 0 เมื่อส่งครบ 3 ครั้ง Device จะตัดการเชื่อมต่อจาก Platform คำนวนปริมาณ Trigger & Action ที่ถูกใช้ไปได้ดังนี้

	|

	Device Online ทำ action ``LINENOTIFY`` และ ``myApp`` = 2 Operations

	|

	ส่งอุณหภูมิ (temp) ครั้งที่ 1 ค่าเป็น 1 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น True = 1 Operations
	ส่งอุณหภูมิ (temp) ครั้งที่ 2 ค่าเป็น 0 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น False = 0 Operations
	ส่งอุณหภูมิ (temp) ครั้งที่ 3 ค่าเป็น -1 ทำ action ``checkTemp`` ตรวจสอบเงื่อนไขและค่าเป็น False = 0 Operations

	|

	Device Offline (``DEVICE.STATECHANGED``) ทำ action ``LINENOTIFY`` และ ``myApp`` = 2 Operations

	|

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
