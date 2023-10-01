# API DOCUMENTATION

> Available Routes: BASE_URL: http://kamvamindpal.com/v1

### /users

#### POST: create a new user, existing user will not return any error

- body: 'email', 'name'.
- header: null

> reqeust:

```bash
curl -si http://kamvamindpal.com/v1/users -X POST -H 'content-type: application/json' -d '{"email":"johndoe@mail.com", "name":"John Deo"}'
```

>

> response:

```json
HTTP/1.1 201 CREATED
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 19 Sep 2023 20:00:16 GMT
Content-Type: application/json
Content-Length: 241
Connection: keep-alive
Vary: Cookie

{
  "data": {
    "created_at": "2023-09-19 20:00:16.894757",
    "email": "johndoe@mail.com",
    "id": "4c4fc6e6-1035-4072-9257-da150c23cb45",
    "name": "John Deo",
    "updated_at": "2023-09-19 20:00:16.894223"
  },
  "message": "User created successfully",
  "status": "success"
}

```

>

### /questions

#### GET: returns a list (25 questions) of quiz questions

- body: null
- header: null

> request:

```bash
curl -si http://kamvamindpal.com/v1/questions
```

> response:

```json
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 19 Sep 2023 20:03:07 GMT
Content-Type: application/json
Content-Length: 8361
Connection: keep-alive
Vary: Cookie

{
  "data": {
    "count": 3,
    "questions": [
      {
        "answers": [
          {
            "id": "1cb3ffc4-2010-4bd6-ab31-26a9fde1685c",
            "text": "Paul"
          },
          {
            "id": "470ef1c7-c5cc-425b-a32a-87158b70e522",
            "text": "Silas"
          },
          {
            "id": "a0d6e835-3080-4591-ae10-9c7271e31a14",
            "text": "Peter"
          },
          {
            "id": "db0d13ef-1ba0-4945-8b0b-d7c6c64cdacd",
            "text": "Jesus Christ"
          }
        ],
        "id": "f015320d-4a71-4bf7-9874-449b639a56c1",
        "text": "Who was grieved in the spirit and he commanded the evil spirit of divination out?"
      },
      {
        "answers": [
          {
            "id": "879ae339-4dac-4515-a0fd-8be6136e0447",
            "text": "David"
          },
          {
            "id": "9adc2378-30f5-41a3-981d-2e74d8e438c0",
            "text": "Saul"
          },
          {
            "id": "e0655144-21dd-4dab-b27c-b79907fe33c8",
            "text": "Aaron"
          },
          {
            "id": "e8cb6e00-3ad4-42dd-aa8f-6d10febabd6b",
            "text": "Samuel"
          }
        ],
        "id": "09af20cb-6929-4516-9707-da81f659557e",
        "text": "Who was to fulfill the prophecy which was given to Moses that the LORD was going to destroy the Amalekites and he disobeyed God?"
      },
      {
        "answers": [
          {
            "id": "1c4bbef1-556d-48e2-8b2d-89ccfc00ffa9",
            "text": "Romans 12 v 2"
          },
          {
            "id": "21599d84-98e8-48b9-92cf-a009a7adb7fa",
            "text": "John 3 v 16"
          },
          {
            "id": "7883d779-1cec-4881-b0c9-ed1e6d6571f3",
            "text": "Ephesians 3 v 20"
          },
          {
            "id": "e8bc626e-a63b-47fe-baa4-0a556ad4797d",
            "text": "1 Corinthians 4 v 20"
          }
        ],
        "id": "660f395b-2232-41c3-becf-00c13d97efb5",
        "text": "And do not be conformed to this world, but be transformed by the renewing of your mind, that you may prove what is that good and acceptable and perfect will of God."
      }
    ]
  },
  "message": "Questions retrieved successfully",
  "status": "success"
}

```

#### POST: recieves an object of `{ key(question_id) : value(answer_id) }` data for submission.

- body:`{ question_id : answer_id, question_id : answer_id,}`
- header: email

> request:

```bash
curl -si http://kamvamindpal.com/v1/questions -X POST -H 'content-type: application/json' -H 'email: johndoe@mail.com' -d '{"f015320d-4a71-4bf7-9874-449b639a56c1":"a0d6e835-3080-4591-ae10-9c7271e31a14","09af20cb-6929-4516-9707-da81f659557e":"9adc2378-30f5-41a3-981d-2e74d8e438c0", "660f395b-2232-41c3-becf-00c13d97efb5":"1c4bbef1-556d-48e2-8b2d-89ccfc00ffa9"}'
```

> response:

```json
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 19 Sep 2023 20:10:29 GMT
Content-Type: application/json
Content-Length: 1788
Connection: keep-alive
Vary: Cookie

{
  "data": {
    "count": 3,
    "questions": [
      {
        "answers": [
          {
            "id": "1cb3ffc4-2010-4bd6-ab31-26a9fde1685c",
            "text": "Paul"
          },
          {
            "id": "470ef1c7-c5cc-425b-a32a-87158b70e522",
            "text": "Silas"
          },
          {
            "id": "a0d6e835-3080-4591-ae10-9c7271e31a14",
            "text": "Peter"
          },
          {
            "id": "db0d13ef-1ba0-4945-8b0b-d7c6c64cdacd",
            "text": "Jesus Christ"
          }
        ],
        "correct_answer": "1cb3ffc4-2010-4bd6-ab31-26a9fde1685c",
        "id": "f015320d-4a71-4bf7-9874-449b639a56c1",
        "text": "Who was grieved in the spirit and he commanded the evil spirit of divination out?",
        "user_answer": "a0d6e835-3080-4591-ae10-9c7271e31a14"
      },
      {
        "answers": [
          {
            "id": "879ae339-4dac-4515-a0fd-8be6136e0447",
            "text": "David"
          },
          {
            "id": "9adc2378-30f5-41a3-981d-2e74d8e438c0",
            "text": "Saul"
          },
          {
            "id": "e0655144-21dd-4dab-b27c-b79907fe33c8",
            "text": "Aaron"
          },
          {
            "id": "e8cb6e00-3ad4-42dd-aa8f-6d10febabd6b",
            "text": "Samuel"
          }
        ],
        "correct_answer": "9adc2378-30f5-41a3-981d-2e74d8e438c0",
        "id": "09af20cb-6929-4516-9707-da81f659557e",
        "text": "Who was to fulfill the prophecy which was given to Moses that the LORD was going to destroy the Amalekites and he disobeyed God?",
        "user_answer": "9adc2378-30f5-41a3-981d-2e74d8e438c0"
      },
      {
        "answers": [
          {
            "id": "1c4bbef1-556d-48e2-8b2d-89ccfc00ffa9",
            "text": "Romans 12 v 2"
          },
          {
            "id": "21599d84-98e8-48b9-92cf-a009a7adb7fa",
            "text": "John 3 v 16"
          },
          {
            "id": "7883d779-1cec-4881-b0c9-ed1e6d6571f3",
            "text": "Ephesians 3 v 20"
          },
          {
            "id": "e8bc626e-a63b-47fe-baa4-0a556ad4797d",
            "text": "1 Corinthians 4 v 20"
          }
        ],
        "correct_answer": "1c4bbef1-556d-48e2-8b2d-89ccfc00ffa9",
        "id": "660f395b-2232-41c3-becf-00c13d97efb5",
        "text": "And do not be conformed to this world, but be transformed by the renewing of your mind, that you may prove what is that good and acceptable and perfect will of God.",
        "user_answer": "1c4bbef1-556d-48e2-8b2d-89ccfc00ffa9"
      }
    ],
    "score": 2
  },
  "message": "Questions graded successfully",
  "status": "success"
}

```
