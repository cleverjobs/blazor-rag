# Unable to set id, name, css, etc on TelerikAutoComplete.

## Question

**Mat** asked on 03 Feb 2020

As stated in the title, I am unable to set id, name, css, etc on TelerikAutoComplete control. For accessibility we need to set an id and link it with the label. Any guidance for handling these scenarios? Is there a standard I am missing for setting these values across all input type controls?

## Answer

**Marin Bratanov** answered on 04 Feb 2020

Hello Mattew, We are working on exposing ID attributes. In the meantime, you can wrap the component in the label, like this: <label> label text <TelerikAutoComplete /> </label> A Class parameter is already available and it sets the desired CSS class to the wrapping element of the component. Regards, Marin Bratanov
