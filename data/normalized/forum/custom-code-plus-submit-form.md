# Custom code plus submit form

## Question

**Dea** asked on 25 Mar 2021

Hi. I have a form that posts to a payment platform. I'd like to have a button that submits the form but also runs some other code, e.g. set a property to hide elements on the page. Can I do this? If so should I use ButtonType="ButtonType.Submit" plus an OnClick? This doesn't seem to work. Or should I use a ButtonType.Button and use some code to post the form? (If so how could I do that)? Thanks. Dean

## Answer

**Stamo Gochev** answered on 30 Mar 2021

Hello, If you are using the standard blazor form then you can use the "OnSubmit" event as explained in the docs to run some code when the form is actually submitted. On the other hand, the same can be achieved with TelerikForm component and its "OnSubmit" event if you are using it instead. A similar scenario can be handled by using the "OnClick" event handler of the button if you do not need to depend on the functionality of the form. As this is expected to work, can you send me a runnable example, which demonstrates the issue you are facing, so I can inspect it? Regards, Stamo Gochev Progress Telerik

### Response

**Dean** answered on 30 Mar 2021

Apologies, I should have been clearer. This is a standard HTML form, and AFAIK it has to be, because it posts to an external URL (a payment gateway). I assume I can't use a Blazor form or Telerik form for that purpose? So I am stuck with an HTML form, but want some way to run code as it submits (just to hide the submit button). Is this possible with a TelerikButton?

### Response

**Stamo Gochev** answered on 02 Apr 2021

Hi, The blazor form and TelerikForm components do not post to a concrete remote URL by default, but it is still possible to use their event handlers to make an API call to a remote endpoint. Using a standard <form> HTML element does not provide any integration with the blazor framework out of the box, so things like validation will not be handled. In this scenario, it is not that important if TelerikButton with ButtonType="Submit" is used or not as it will behave as the standard <button> HTML element (including its @onclick event). One more option you can try is using the native "submit" event of the form to execute additional logic (<form @onsubmit="..."></form>). Regards, Stamo Gochev Progress Telerik
