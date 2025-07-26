# Required field indicator for FormItems

## Question

**Kev** asked on 14 Aug 2024

Looking to leverage the Required data annotation on the model to apply an asterisk or other required field indicator to a FormItem's label. Is there a way to apply an html attribute/class to a FormItem automatically, that could then be used to append an asterisk to its label? Trying to avoid the need of marking Required both in the model and the UI.

## Answer

**Dimo** answered on 15 Aug 2024

Hello Kevin, As a UI component vendor we focus on the UI. On the other hand, there can be a lot of different ways to signify a required field. Although the asterisk is a common approach, it is by no means universally accepted or understandable. Every customer may even want the asterisk to look differently. That's why we have decided not to provide such automatic UI out-of-the-box. So, you are right that you need to either define (hard-code) the required items in the UI or use reflection to get the DataAnnotations attributes for each Field and then append asterisks to the FormItem LabelText parameter or in the FormItem Template. Regards, Dimo
