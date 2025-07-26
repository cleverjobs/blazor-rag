# Waitcursor/spinner for button

## Question

**Lar** asked on 19 Jan 2021

Is there some way to change a button to have an animated spinning gif after clicking it invokes either a data retrieval or does an update? Something like this (with the boolean as a property in code-behind)? <TelerikButton OnClick="@(args=> NameOfFunction(param1, param2, param))">Retrieve <template> @if(IsSaving==false) { //Leave button as is } else { //Put animated spinning gif } </template> </TelerikButton>

### Response

**billy** commented on 23 Nov 2022

He's not wanting to show a loader on the screen "somewhere" but instead swap an icon within the button to be a loader while performing an action. I am needing to do something like this as well and the compile fails. This is baked in behavior in other frameworks like material and bootstrap. Is this not a possibility?

### Response

**Dimo** commented on 25 Nov 2022

@Billy - the previously linked Loader Overview page contains a "Using In Other Components" section with an example of a Loader inside a Button.

## Answer

**Svetoslav Dimitrov** answered on 20 Jan 2021

Hello Larry, We have a Loader component that you can use to add a spinner or other type of loader to your Telerik Button. We have an example that shows how to achieve that in the Visible parameter section of the docs. Regards, Svetoslav Dimitrov
