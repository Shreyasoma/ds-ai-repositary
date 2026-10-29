TYPES OF DATA

The problem, A food delivery app wants to improve. It holds:
- a table of orders (order ID, customer ID, amount, time)
- the data its app sends to the server for each order, saved as nested { "key": "value" } records, where some orders have a "coupon" field and others don’t
- thousands of written customer reviews
- photos customers upload of their meals

1. Structured data: fixed rows and columns, where every record has the same fields. Examples: SQL tables, CSV files, Excel sheets. Easy to query and analyze.
2. Semi-structured data: it has labels or tags (keys), but the fields can vary between records, and records can be nested. Examples: JSON, XML. You need to parse it before analysis.
3. Unstructured data: no predefined format. Examples: free text, images, audio, video. It needs special techniques (NLP, computer vision) to extract anything usable.

Classify each as structured, semi-structured or unstructured, with a one-line reason:
1. A SQL table of employees (ID, name, salary, department) 
- Structured: It has fixed rows and columns with the same fields for every employee.
2. The JSON response you get from a weather API
- Semi-structured: It uses keys and values, and its fields can vary.
3. A customer’s written review of a product
- Unstructured: It is free text without a fixed format.
4. CCTV video footage from a shop
- Unstructured: It contains video and does not follow a fixed table format.
5. An email (it has To, From and Subject fields, plus a free-text body)
- Semi-structured: It has fixed fields like To, From, and Subject, along with a free-text body.
6. Harder: Ravi’s handwritten sales notebook. What type is it? What would he have to do to turn it into something you could analyze with Python?
- It is unstructured because the information is handwritten and may not follow a consistent format. Ravi should enter the sales records into an Excel or CSV file with columns like date, cups sold, and milk used. Then he can load the file into Python for analysis.