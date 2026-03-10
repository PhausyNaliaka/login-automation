# Login Page Test Cases

## Test Case 1: Valid Login

**Steps**
1. Open login page
2. Enter email: test@test.com
3. Enter password: 123456
4. Click login

**Expected Result**
User should be redirected to dashboard page.


---

## Test Case 2: Invalid Password

**Steps**
1. Open login page
2. Enter email: test@test.com
3. Enter password: wrong123
4. Click login

**Expected Result**
Error message should appear: "Invalid email or password"


---

## Test Case 3: Empty Email

**Steps**
1. Open login page
2. Leave email empty
3. Enter password
4. Click login

**Expected Result**
Login should fail and show error.


---

## Test Case 4: Empty Password

**Steps**
1. Open login page
2. Enter email
3. Leave password empty
4. Click login

**Expected Result**
Login should fail.


---

## Test Case 5: SQL Injection Attempt

**Steps**
1. Enter email: ' OR '1'='1
2. Enter password: anything
3. Click login

**Expected Result**
Login should fail.