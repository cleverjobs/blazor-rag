# Calling SetState on TreeList does not trigger OnStateChanged

## Question

**TedTed** asked on 08 Jul 2022

Calling SetState on a TreeList does not trigger the OnStateChanged event. I thought the whole point of the OnStateChanged event was to have a central location to capture state change actions on a TreeList? How are we supposed to capture and execute code when SetState is called to change the state of the TreeList?

### Response

**Dimo** commented on 12 Jul 2022

UI component events fire as a result of user actions, not developer actions. This is a general programming principle. It's the same with a regular <input> element - it will not fire a change event if you set its value programmatically. In your case, implement your business logic before or after the SetState() call.
