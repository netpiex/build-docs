.. raw:: html

    <div align="right"><b>TH</b> | <a href="https://docs.netpie.io/en/coap-netpie.html">EN</a></div>

CoAP API
==========

|

CoAP (Constrained Application Protocol) เป็น Protocol ประเภทหนึ่งคล้ายกับ HTTP แต่ HTTP จะเป็น TCP ส่วน CoAP จะเป็น UDP ซึ่งถูกพัฒนาขึ้นเพื่อลดขนาดแพคเกจข้อมูลที่ส่งให้เล็กลง ช่วยให้ลดการใช้ทรัพยากรทั้งหน่วยความจำในการประมวลผลและพลังงาน จึงเหมาะสำหรับ Microcontroller ที่มีหน่วยความจำไม่มากหรือต้องการประหยัดพลัง เช่น NB-IoT โดยมี Endpoint หลัก คือ |coap_url| มีรายละเอียดดังนี้

|

ตัวอย่างการใช้งานในที่นี้จะอยู่ในรูปแบบ Command Line ใช้ NodeJS สำหรับการติดตั้ง CoAP Client (ติดตั้ง NodeJS https://nodejs.org/en/download/) โดยการติดตั้ง CoAP Client ให้รันด้วยคำสั่งต่อไปนี้ใน (เวอร์ชัน CoAP Client ที่รองรับต้องไม่เกิน 0.5.1)

|

``npm i coap-cli@0.5.1 -g``

|

**1. การ Publish ข้อความ ไปที่ Topic ต่างๆ**

|

.. list-table::
	:widths: 20 80

	* - **EndPoint**
	  - |coap_url|/message/{any}/{topic}
	* - **Method**
	  - PUT
	* - **Parameter**
	  - auth=<ClientID>:<Token>
	* - **Payload**
	  - -p message
	* - **Return**
	  - Response Code ในที่นี้จะเป็น ``undefined`` เนื่องจาก Code ที่ส่งกลับมาไม่มีการกำหนดค่าไว้

ตัวอย่าง (Command Line) 

.. code-block:: console

	coap put "coap://coap.netpie.io/message/home/bedroom?auth=6c36fdee-5273-4318-xxxx-75dfd2c513db:nzxGsGMYnFdfET6xxxxfb32U9z5kuhvx" -p "Hello from CoAP"

จากตัวอย่างด้านบน เป็นการ Publish ข้อความ ``Hello from CoAP`` ไปที่ Topic ``@msg/home/bedroom`` 

|

**2. การอ่านข้อมูล Shadow Data ของ Device**

|

.. list-table::
	:widths: 20 80

	* - **EndPoint**
	  - |coap_url|/shadow/data
	* - **Method**
	  - GET
	* - **Parameter**
	  - auth=<ClientID>:<Token>
	* - **Return**
	  - Response Object {``deviceid`` => ClientID, ``data`` => Shadow Data ของ Device (JSON), ``rev`` => Revision ของ Shadow, ``modified`` => Timestamp การแก้ไขล่าสุด}

ตัวอย่าง (Command Line) 

.. code-block:: console

	coap get "coap://coap.netpie.io/shadow/data?auth=6c36fdee-5273-4318-xxxx-75dfd2c513db:nzxGsGMYnFdfET6xxxxfb32U9z5kuhvx"

จากตัวอย่างด้านบน เป็นการอ่านข้อมูล Shadow ของ Device ID : 6c36fdee-5273-4318-xxxx-75dfd2c513db และค่าที่ได้กลับมา คือ

.. code-block:: json
	
	{
		"deviceid":"6c36fdee-5273-4318-xxxx-75dfd2c513db",
		"data": {
			"humid":76.2, "temp":25
		},
		"rev":3,
		"modified":1605516471534
	}

|

**3. การเขียนข้อมูลลง Shadow Data แบบเขียนผสาน (Merge)**

|

.. list-table::
	:widths: 20 80

	* - **EndPoint**
	  - |coap_url|/shadow/data
	* - **Method**
	  - PUT
	* - **Parameter**
	  - auth=<ClientID>:<Token>
	* - **Payload**
	  - -p {data: { Shadow Data (JSON) }}
	* - **Return**
	  - Response Object {``deviceid`` => ClientID, ``data`` => Shadow Data ของ Device (JSON), ``modified`` => Timestamp การแก้ไขล่าสุด, ``timestamp`` => Timestamp ที่ใช้กำกับจุดข้อมูลกรณีมีการเก็บลง Time-series data storage}

ตัวอย่าง (Command Line)  

.. code-block:: console

	coap put "coap://coap.netpie.io/shadow/data?auth=6c36fdee-5273-4318-xxxx-75dfd2c513db:nzxGsGMYnFdfET6xxxxfb32U9z5kuhvx" -p "{data: {temp: 30.4} }"

จากตัวอย่างด้านบน เป็นการเขียนข้อมูล Shadow แบบผสาน (Merge) ของ Device ID : 6c36fdee-5273-4318-xxxx-75dfd2c513db และค่าที่ได้กลับมา คือ

.. code-block:: json
	
	{
		"deviceid":"6c36fdee-5273-4318-xxxx-75dfd2c513db",
		"data": {
			"temp":30.4
		},
		"modified":1605518877506,
		"timestamp":1605518877506
	}

|

.. _key-shadow-batch-coap:

Shadow Batch Update
--------------------

|

จะใช้ในกรณีที่ IoT Device ไม่สามารถส่งข้อมูลขึ้น Cloud Platform ได้ตามเวลาที่กำหนด เช่น อาจจะเกิดจากปัญหาการเชื่อมต่ออินเตอร์เน็ต เป็นต้น ทำให้ IoT Device จำเป็นต้องเก็บข้อมูลไว้ที่หน่วยความจำของ Device เองก่อน เช่น เก็บลง SD Card เป็นต้น และเมื่อสามารถเชื่อมต่อ Cloud Platform ได้ จึงทำการส่งข้อมูลที่เก็บไว้ทั้งหมดขึ้น Cloud Platform อีกที โดยสามารถส่งค่าขึ้น Platform ครั้งละหลาย ๆ จุดพร้อมกันได้

|

การเขียน Shadow แบบ Batch ทำได้ 3 ช่องทาง ได้แก่

|

1. CoAP API คือ การเขียนข้อมูลเป็น Batch โดยดำเนินการผ่าน CoAP Protocol ซึ่งสามารถเขียนได้ทั้งแบบผสาน (Merge) หรือเขียนทับ (Overwrite) มีรายละเอียดดังนี้

|

.. list-table::
	:widths: 20 80

	* - **EndPoint**
	  - |coap_url|/shadow/batch
	* - **Method**
	  - PUT (กรณี Merge) หรือ POST (กรณี Overwrite)
	* - **Parameter**
	  - auth=<ClientID>:<Token>
	* - **Payload**
	  - -p {"ackid" : ID value, "batch" : [ {"data":{ Shadow Data 1 }, "ts": time 1}, {"data":{ Shadow Data 2 }, "ts": time 2}, ...,{"data":{ Shadow Data n }, "ts": time n} ], "merged": true or false }
	* - **Return**
	  - Response Object {``deviceid`` => ClientID, ``response`` => สรุปข้อมูลการอัพเดท Shadow (JSON)}

|

ตัวอย่าง (Command Line)  

.. code-block:: console

	coap put "coap://coap.netpie.io/shadow/batch?auth=6c36fdee-5273-4318-xxxx-75dfd2c513db:nzxGsGMYnFdfET6xxxxfb32U9z5kuhvx" -p '{"ackid" : 1234,"batch" : [{"data":{"humid":9.6}, "ts":-90000},{"data":{"humid":9.8}, "ts":-60000},{"data":{"humid":9.1}, "ts":-30000},{"data":{"temp":26.8}, "ts":0}]}'

จากตัวอย่างด้านบน เป็นการเขียนข้อมูล Shadow แบบ Batch แบบผสาน (Merge) ของ Device ID : 6c36fdee-5273-4318-xxxx-75dfd2c513db และค่าที่ได้กลับมา คือ

.. code-block:: json
	
	{
		"deviceid":"6c36fdee-5273-4318-xxxx-75dfd2c513db",
		"response": {
			"ackid":1234,
			"total":4,
			"mints":1619088626897,
			"maxts":1619088716897
		}
	}

|

.. note:: 

	เวลาที่กำกับของแต่ละชุดข้อมูลมีหน่อยเป็น Millisecond สามารถใช้คำว่า ts หรือ timestamp เป็นชื่อฟิลด์ก็ได้ หากมีค่าต่ำกว่า 1000 * 2^23 = 8388608000 จะถือว่าเป็นค่า Relative Time กับเวลาปัจจุบัน ถ้ามีค่ามากกว่า จะถือเป็น timestamp แบบ Absolute Time สามารถใช้ค่าลบแทนเวลาในอดีตได้ ซึ่งจะเหมาะสำหรับการอัพเดตข้อมูลจุดย้อนหลัง ยกตัวอย่างเช่น ถ้ากำหนด ts หรือ timestamp เป็น -90000 และ timestamp ปัจจุบัน คือ 1619075885 เวลาที่เกิดจุดข้อมูลนั้นจะเป็น 1619075885 - 90000 = 1618985885 (เวลาย้อนหลังไปจากปัจจุบัน 90 วินาที)

	ackid ใช้เป็นค่าอ้างอิงการตอบกลับของแต่ละ Request ตั้งเป็นค่าอะไรก็ได้ เป็นได้ Number หรือ String โดยทุกการตอบกลับจะมีการทวนค่า ackid เดิม เพื่อให้ผู้ใช้สามารถจับคู่ระหว่าง Request และ Response ได้

	|

	ในส่วนของฟิลด์ ``merged`` ที่ระบุอยู่ใน Request Body เพื่อส่งไปเขียนลง Shadow เป็นการกำหนดรูปแบบการเขียนข้อมูลว่าจะเขียนแบบผสาน (Merge) หรือแบบเขียนทับ (Overwrite) ถ้าเซ็ต ``merged : true`` จะเป็นการเขียนแบบผสาน (Merge) และถ้าเซ็ต ``merged : false`` จะเป็นการเขียนแบบเขียนทับ (Overwrite) แต่ถ้าไม่มีการระบุค่านี้ลงใน Request Body ระบบจะดูจาก Method ที่เลือกใช้ในการ Request ครั้งนั้น ๆ ว่าเป็น PUT (เขียนแบบ Merge) หรือ POST (เขียนแบบ Overwrite) กรณีที่มีการใช้ Method ขัดแย้งกับฟิลด์ ``merged`` ระบบจะให้ความสำคัญสูงสุดกับฟิลด์ ``merged`` โดยไม่สนใจ Method ของ Request

	|

	การทำงานของ Expression ที่กำหนดไว้ใน Schema และ Trigger กรณีเขียน Shadow แบบ Batch

	Expression ยังคงถูกคำนวณตามสูตรที่กำหนดไว้ทุกชุดข้อมูล เหมือนการ For Loop เขียน Shadow เอง แต่การเขียน Shadow แบบ Batch จะถูกหักโควต้า Shadow read/write เพยีง 1 Operation เท่านั้น แต่โควต้า Shadow Expression จะถูกหักตามจำนวนชุดข้อมูลเช่นเดิม ยกตัวอย่างเช่น ชุดข้อมูลที่ส่งค่ามาบันทึก 100 จุด และมีฟิลด์ข้อมูลที่เซ็ต Expression ไว้ 1 ฟิลด์ จำนวน Shadow Expression ที่ถูกหักจะเท่ากับ 1 x 100 = 100 Operations เป็นต้น

	สำหรับ Trigger จะทำงานเฉพาะชุดข้อมูลที่เป็นค่าล่าสุด (Timestamp มีค่าสูงสุด) เท่านั้น และจะถูกหักโควต้าการใช้งานเหมือนการเขียนข้อมูลแค่ชุดเดียว

|

2. MQTT คือ การเขียนข้อมูลเป็น Batch จะใช้ Topic และ Payload ดูรายละเอียดได้ที่ :ref:`key-shadow-batch-mqtt`

|

3. REST API คือ การเขียนข้อมูลเป็น Batch โดยดำเนินการผ่าน REST API ซึ่งสามารถเขียนได้ทั้งแบบผสาน (Merge) หรือเขียนทับ (Overwrite) เช่นกัน ดูรายละเอียดได้ที่ :ref:`key-shadow-batch-rest`

|

.. caution::

	ข้อจำกัดของการเขียน Shadow แบบ Batch คือ จำนวนชุดข้อมูลที่ส่งไปเขียนได้ต่อครั้งต้องไม่เกิน 100 ชุดข้อมูล (JSON Array ของฟลิด์ ``batch``) เช่น กำหนด Payload ที่ส่งไปเขียนข้อมูลเป็น 

	{ "ackid" : 1234, "batch" : [ {"data":{"temp":25.9, "humid":9.6}, "ts":-90000}, {"data":{"temp":25.3, "humid":9.8}, "ts":-60000}, {"data":{"temp":24.5, "humid":9.1}, "ts":-30000}, {"data":{"temp":26.8, "humid":8.2}, "ts":0}], "merged": true } 

	แสดงว่ามีจำนวนชุดข้อมูลเท่ากับ 4 ชุดข้อมูล เป็นต้น หากมีส่งชุดข้อมูลไปเกินกว่าที่กำหนด ข้อมูลทั้งหมดจะไม่ถูกบันทึก และจะมีข้อความแจ้งเตือนกลับมาในรูปแบบ JSON ดังนี้ 

	{"ackid":1234,"errcode":429,"message":"batch size exceeds 100","inputsize": 102} 

	หมายความว่า การเขียนข้อมูลแบบ Batch ที่ ackid เป็น 1234 ส่งชุดข้อมูลไปเกิน 100 ชุด โดยส่งไป 102 ชุด เป็นต้น