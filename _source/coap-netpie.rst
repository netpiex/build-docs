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
