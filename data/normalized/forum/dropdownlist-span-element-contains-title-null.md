# dropdownlist span element contains title="null"

## Question

**RobRob** asked on 22 Mar 2022

When using the TelerikDropDownList component in Blazor, the html generated sometimes contains title="null" in the outer span element. This then shows up as a tooltip of null when hovering the dropdownlist control on the rendered page. What could be causing this and is there a way of suppressing it? Thank you.

### Response

**Rob** commented on 24 Mar 2022

It looks like this bug is in the TelerikValidationTooltip as we have now seen this behaviour with other input controls/components such as text boxes, check boxes, date pickers, etc. The problem occurs after a validation error has been corrected.

## Answer

**Dimo** answered on 08 Apr 2022

Hi Rob, I am pasting a link to new public bug report for the other developers to see. Regards, Dimo
