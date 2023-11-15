# {{PROBLEM}} Function Design Recipe

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

## 1. Describe the Problem

Need to check if a given text includes a specific string 'TODO'

## 2. Design the Function Signature

Function name: to_do_checker
Parameters: string (text)
Return value: Boolean (True if the text does include 'TODO', False otherwise)

Side Effects:
This function will not print anything of have any other side-effects

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

1. If given an empty string, returns an error "No text has been inputted"

test_to_do_checker("") => Error message

2. If given a text with "TODO" included, returns True

test_to_do_checker("TODO: Walk the Dog") => True

3. If given a text without "TODO" included, returns False

test_to_do_checker("Shopping List") => False

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