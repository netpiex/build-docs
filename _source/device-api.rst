RESTful API
============

|

เป็นช่องทางสำหรับให้ Device เรียกใช้บริการ Platform ผ่าน RESTful API ซึ่งใช้ HTTP Protocal เหมาะสำหรับใช้เป็นช่องทางในการผสานรวม (Integration) ระบบต่างๆ ทั้งที่มีอยู่แล้วหรือกำลังจะพัฒนาขึ้นมาใหม่ โดยไม่จำกัดว่าจะต้องพัฒนาจากภาษาโปรแกรมใด |swagger_part| สำหรับ API ที่มีให้บริการในปัจจุบันแยกเป็น 2 กลุ่ม ดังนี้

|

Device API
--------------------

|

เป็น API ที่เกี่ยวข้องกับ Device โดย Domain name ของ API คือ |rest_url| มีรายละเอียดดังนี้

|

**1. การ Publish ข้อความ ไปที่ Topic ต่างๆ สามารถใช้งานได้ 2 แบบ**

- แบบที่ 1 เป็นการระบุ Topic ในรูปแบบ URL Path

:EndPoint: |rest_url|/message/{any}/{topic}

:Method: PUT

:Request Header: Authorization : *Device ClientID:Token*

:Request Body: Content-type : *text/plain*
	
	ข้อความที่ต้องการ Publish ไปที่ Topic

:Return: *Response Object*

	- ``status`` => รหัสตอบกลับ (HTTP Response Code)

	- ``message`` => ข้อความตอบกลับ

:ตัวอย่าง: 
	
	PUT /device/message/mythings/bedroom/light HTTP/1.1

	Host: |rest_url2|

	Authorization: Device 777d5c96-4c83-4aa6-a273-5ee7c5f453b1:abcduKh8r2tP1zVc1W1nG8YWZeu21234

	ON

|

- แบบที่ 2 เป็นการระบุ Topic ผ่าน Parameter (Query String)

:EndPoint: |rest_url|/message

:Method: PUT

:Request Header: Authorization : *Device ClientID:Token*

:Parameter: ``topic`` :*string* คือ Topic ที่ต้องการ Publish ข้อความไปหา ({any}/{topic})

:Return: *Response Object*

	- ``status`` => รหัสตอบกลับ (HTTP Response Code)

	- ``message`` => ข้อความตอบกลับ

:ตัวอย่าง: 
	
	PUT /device/message?topic=mything/bedroom/light HTTP/1.1

	Host: |rest_url2|

	Authorization: Device 777d5c96-4c83-4aa6-a273-5ee7c5f453b1:abcduKh8r2tP1zVc1W1nG8YWZeu21234

	OFF

|

**2. การอ่านข้อมูล Shadow Data ของ Device (ต้องเป็น Device ที่อยู่ใน Group เดียวกัน)**

:EndPoint: |rest_url|/shadow/data

:Method: GET

:Request Header: Authorization : *Device ClientID:Token*

:Parameter: ``alias`` :*string* คือ ชื่อ Device (Device Alias) ของ Shadow ที่ต้องการอ่าน (ถ้าเป็นอ่าน Shadow ของตัวเองไม่ต้องส่ง Parameter นี้ไป)

:Return: *Response Object*

	- ``status`` => รหัสตอบกลับ (HTTP Response Code)

	- ``data`` => Shadow Data ของ Device (JSON)

:ตัวอย่าง: 

	GET /device/shadow/data?alias=sensor HTTP/1.1

	Host: |rest_url2|

	Authorization: Device 777d5c96-4c83-4aa6-a273-5ee7c5f453b1:abcduKh8r2tP1zVc1W1nG8YWZeu21234

**3. การเขียนข้อมูลลง Shadow Data แบบเขียนผสาน (Merge)**

:EndPoint: |rest_url|/shadow/data

:Method: PUT

:Request Header: Authorization : *Device ClientID:Token*

:Parameter: ``alias`` :*string* คือ ชื่อ Device (Device Alias) ของ Shadow ที่ต้องการเขียน (ถ้าเป็นเขียน Shadow ของตัวเองไม่ต้องส่ง Parameter นี้ไป)

:Request Body: 
	
	ข้อมูลที่ต้องการเขียนลง Shadow Data อยู่ในรูปแบบ JSON ดังนี้ ``{data: {field name 1: value1, field name 2: value2, ..., field name n: value n}}``

:Return: *Response Object*

	- ``status`` => รหัสตอบกลับ (HTTP Response Code)

	- ``data`` => ข้อมูลการอัพเดท Device Shadow Data (JSON)

:ตัวอย่าง: 
	
	PUT /device/shadow/data?alias=test HTTP/1.1
	
	Host: |rest_url2|

	Authorization: Device 777d5c96-4c83-4aa6-a273-5ee7c5f453b1:abcduKh8r2tP1zVc1W1nG8YWZeu21234

	{data:{temperature:33.7, config: {item1: a, item2: b}, note: test case}}

**4. การเขียนข้อมูลลง Shadow Data แบบเขียนทับ (Overwrite)**

:EndPoint: |rest_url|/shadow/data

:Method: POST

:Request Header: Authorization : *Device ClientID:Token*

:Parameter: ``alias`` :*string* คือ ชื่อ Device (Device Alias) ของ Shadow ที่ต้องการเขียน (ถ้าเป็นเขียน Shadow ของตัวเองไม่ต้องส่ง Parameter นี้ไป)

:Request Body: 
	
	ข้อมูลที่ต้องการเขียนลง Shadow Data อยู่ในรูปแบบ JSON ดังนี้ ``{data: {field name 1: value1, field name 2: value2, ..., field name n: value n}}``

:Return: *Response Object*

	- ``status`` => รหัสตอบกลับ (HTTP Response Code)

	- ``data`` => ข้อมูลการอัพเดท Device Shadow Data (JSON)

:ตัวอย่าง: 

	POST /device/shadow/data?alias=test HTTP/1.1
	
	Host: |rest_url2|

	Authorization: Device 777d5c96-4c83-4aa6-a273-5ee7c5f453b1:abcduKh8r2tP1zVc1W1nG8YWZeu21234

	{data:{temperature:33.7, config: {item1: a, item2: b}, note: test case}}

|

Data Store API
--------------------

|

เป็น API ที่เกี่ยวข้องกับการดึงข้อมูลที่เก็บอยู่ใน Timeseries Data โดย Domain name ของ API คือ |feed_url| ฐานข้อมูลที่ใช้เก็บ คือ ซึ่งใช้ KairosDB ลักษณะการ Query ข้อมูล Parameter ต่างๆ ที่ส่งไปจะเป็นรูปแบบเดียวกับ KairosDB มีรายละเอียดดังนี้

:EndPoint: |feed_url|/api/v1/datapoints/query

:Method: POST

:Request Header: Authorization : *Bearer UserToken*

	Content-Type : *application/json*

:Request Body: เงื่อนไขที่ใช้ในการ Query อยู่ในรูปแบบ JSON สามารถแยกได้เป็น 2 ประเภท คือ

	*1. Query Properties* ประกอบด้วย

	- ``start_absolute`` => เวลาเริ่มที่มีหน่วยเป็นมิลลิวินาที(milliseconds)

	- ``start_relative`` => เวลาเริ่มที่สัมพันธ์กับเวลาปัจจุบัน โดยนำเวลาปัจจุบันลบด้วยเวลาที่ระบุ ซึ่งระบุเป็นจำนวนและหน่วยของเวลา หน่วยที่เป็นไปได้มี ดังนี้ milliseconds, seconds, minutes, hours, days, weeks, months และ years ตัวอย่างเช่น หากเวลาเริ่มต้นคือ 5 นาที จุดข้อมูลที่ถูกส่งกลับมาจะอยู่ในช่วง 5 นาทีที่ผ่านมา

	- ``end_absolute`` => เวลาสิ้นสุดที่มีหน่วยเป็นมิลลิวินาที(milliseconds) และต้องเป็นเวลาที่มีค่ามากกว่า ``start_absolute``

	- ``end_relative`` => ระบุเวลาสิ้นสุดที่สัมพันธ์กับเวลาปัจจุบัน โดยนำเวลาปัจจุบันลบด้วยเวลาที่ระบุ ซึ่งระบุเป็นจำนวนและหน่วยของเวลา หน่วยที่เป็นไปได้มี ดังนี้ milliseconds, seconds, minutes, hours, days, weeks, months และ years ตัวอย่างเช่น หากเวลาเริ่มต้นคือ 30 นาทีและเวลาสิ้นสุดคือ 10 นาที จุดข้อมูลที่ถูกส่งกลับมาจะอยู่ระหว่าง 30 นาทีล่าสุดจนถึง 10 นาทีสุดท้าย หากไม่ได้ระบุเวลาสิ้นสุดจะถือว่าเป็นวันที่และเวลาปัจจุบัน

	- ``time_zone`` => เขตเวลาสำหรับช่วงเวลาของการ Query ข้อมูล หากไม่ได้ระบุจะใช้ UTC (สำหรับ ``time_zone`` ที่ |platform_name| Platform กำหนดให้จะเป็น GMT)

	** หมายเหตุ ** : ``start_absolute`` และ ``start_relative`` จำเป็นต้องระบุค่า แต่เลือกใช้เพียงค่าใดค่าหนึ่งเท่านั้น ส่วน ``end_absolute`` และ ``end_relative`` จะระบุหรือไม่ก็ได้ ถ้าระบุก็เลือกใช้เพียงค่าใดค่าหนึ่งเช่นเดียวกัน

	|

	*2. Metric Properties* ประกอบด้วย

	- ``name`` => ชื่อของ Metric ที่ต้องการ Query ข้อมูล ให้ระบุเป็น DeviceId (Client ID ของ Device) จาก |platform_name| Platform (ต้องระบุ)

	- ``aggregators`` => Array ของการตั้งค่าการรวมหรือประมวลผลข้อมูลในรูปแบบต่างๆ ก่อนส่งจุดข้อมูลกลับมา ซึ่ง Parameters ที่เกี่ยวข้องมีดังนี้

		- name => ประเภทรูปแบบการประมวลผลข้อมูล ได้แก่ "avg" (Average), "dev" (Standard Deviation), "count", "first", "gaps", "histogram", "last", "least_squares", "max", "min", "percentile", "sum", "diff" (Difference), "div" (Divide), "rate", "sampler", "scale", "trim", "save_as", "filter", "js_function" (JS Aggregator), "js_filter" (JS Aggregator), "js_range" (JS Aggregator) ดูรายละเอียดเพิ่มเติมจาก `kairosdb <https://kairosdb.github.io/docs/build/html/restapi/Aggregators.html>`_

	- ``tags`` => สำหรับกรองข้อมูลที่ต้องการตาม Tag ใน |platform_name| Platform ระบุ Data Field ที่ต้องการ รูปแบบ คือ tags : { attr: [ field_1, field_2, ..., field_n ] }

	- ``group_by`` => จัดกลุ่มจุดข้อมูลที่ Query โดยสามารถจัดตาม Tag, ช่วงเวลา, ค่าจุดข้อมูล หรือตามถังข้อมูล ใน |platform_name| Platform ใช้ Tag ในการจัดกลุ่มข้อมูล (แยกตาม Data Field)

	- ``exclude_tags`` => จะให้แสดง Tag ในข้อมูลที่ส่งกลับมาด้วยหรือไม่ (``true`` คือ แสดง Tag เป็นค่า Default, ``false`` คือ ไม่แสดง Tag)

	- ``limit`` => เป็นการจำกัดจำนวนจุดข้อมูลที่จะ Query โดยจะเป็นการจำกัดจำนวนจุดข้อมูลจริงก่อนจะทำ ``aggregators``

	- ``order`` => การเรียงลำดับจุดข้อมูล (``asc`` คือ เรียงจากน้อยไปมาก, ``desc`` คือ เรียงจากมากไปน้อย) โดยจะเรียงลำดับจุดข้อมูลจริงก่อนจะทำ ``aggregators``

:Return: *Response Object*

	ดึงข้อมูลสำเร็จ (status : 200)

		ข้อมูลที่ Query ได้อยู่ในรูปแบบ JSON

	ดึงข้อมูลล้มเหลว (status : 400 หรือ 500)

		- 400 Bad Request => คำขอไม่ถูกต้อง เช่น ส่ง Parameter ไม่ครบหรือไม่ถูกต้อง

		- 500 Internal Server Error => หากเกิดข้อผิดพลาดในการเรียกข้อมูลทางฝั่ง Server


:ตัวอย่าง: 

	POST /api/v1/datapoints/query HTTP/1.1

	Host: |feed_url2|

	Authorization: Bearer AyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.AyJjdHgiOnsib3duZXIiOiJVOTc0ODE0NzczMjA0In0sInNjb3BlIjpbXSwiaWF0IjoxNTcxMzc1ODk4LCJuYmYiOjE1NzEzNzU4OTgsImV4cCI6MTU3MTQ2MjI5OCwiZXhwaXJlSW4iOjg2NDAwLCJqdGkiOiIzRk50VkVmVCIsImlzcyI6ImNlcjp1c2VydG9rZW4ifQ.AtbhSRgGXCjiQk4wENMD4KQ3ufDof7HnzHY5Rcli0y0LpTJEDLklM-AmsAVzBnPBnJh9L3LvSGODc9xrYWotcA

	Content-Type: application/json

	{ "start_relative": { "value":1, "unit":"days" }, "metrics":[{ "name":"Aaa5d93b-Ae16-455f-A854-335AAAA16256", "tags":{"attr":["temp", "humit"]}, "limit":50, "group_by":[{ "name":"tag", "tags":["attr"] }], "aggregators":[{ "name":"avg", "sampling":{ "value":"1", "unit":"minutes" } }] }] }
