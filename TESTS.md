# Archstart Tests

Manual System Tests for the Archstart CLI

### Test 1
Generate a Main/Subroutine Python Program

1. Run the CLI
```bash
python3 [path to archstart/archstart]/archstart.py
```
2. Enter a Program Name
```bash
test_script.py
```
3. Select Main/Subroutine Architecture
```bash
0
```
4. Enter Number of Subroutines
```bash
3
```
5. Verify that a new file called `test_script.py` is populated with three subroutines and one main function.


### Test 2
Generate a Publisher/Subscriber Python Program

1. Run the CLI
```bash
python3 [path to archstart/archstart]/archstart.py
```
2. Enter a Program Name
```bash
test_script.py
```
3. Select Publisher/Subscriber Architecture
```bash
1
```
4. Enter Number of Subscribers
```bash
3
```
5. Enter Number of Publishers
```bash
3
```
6. Enter Number of Topics
```bash
1
```
7. Verify that a new file called `test_script.py` is populated with three publishers, three subscribers, and one topic.


### Test 3
Generate a Client Server Python Program

1. Run the CLI
```bash
python3 [path to archstart/archstart]/archstart.py
```
2. Enter a Program Name
```bash
test_script.py
```
3. Select Client Architecture
```bash
2
```
4. Verify that new files called `test_script_client.py` and `test_script_server.py` are now populated.
