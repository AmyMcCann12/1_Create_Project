# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user, they don't have a current estimate of how long it takes to read a text.

## 2. Design the Function Signature

Function name: get_reading_time
Parameters: 1. Text to measure 2. Reading speed(number of words per minute)
Return value: time (in minutes) as a float

Side Effects:
Text to measure could be very long.
This function will not print anything of have any other side-effects


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

get_reading_time("", 200) => 0

get_reading_time(sentence with 5 words, 200) => 5/200 

get_reading_time(sentence with 5 words, 100) => 5/100

get_reading_time(sentence with large number of words, 200) => number of words / 200

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->