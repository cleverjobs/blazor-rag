# Disable automatic Fluentvalidation in a form

## Question

**Arn** asked on 22 Dec 2023

Hi, I have a TelerikForm containing a Fluent Validator and 2 buttons. Only one of them has to validate the form. However, even if I set NO code into the button's associated method, it does trigger the validation. Seems to be a default behaviour. How to disable it for my second button? Thx in advance A

## Answer

**Radko** answered on 25 Dec 2023

Hi Arnaud, I have no repro, but my guess is that there is no explicit type set to the button, meaning it defaults to the submit. If this is so, then each click the button would attempt to submit the form, thus triggering validation. If you are using our Button component, then pass a value to the ButtonType parameter: <TelerikButton ButtonType="ButtonType.Button " OnClick="@ClickHandler"> Click me </TelerikButton> if you are using a plain HTML button tag, then set the type attribute: <button type="button"> Click me </button> If my guess was incorrect and this did not resolve the issue, would you be able to send a repro, so we can look into this further? Thank you. Regards, Radko Progress Telerik

### Response

**Arnaud** commented on 03 Jan 2024

Hi Radko, Indeed, this was my problem, thx a lot for pointing it out :) Have a gd day. A
