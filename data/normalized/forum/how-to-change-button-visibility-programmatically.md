# How to change button visibility programmatically?

## Question

**Sea** asked on 04 Sep 2019

I am trying to use a Window component with Telerik buttons to allow the user to both make choices and to acknowledge. If they need to make a choice, I want two buttons. If they need to acknowledge, I want one button. But the properties of the button don't allow them to be changed programatically. How to accomplish this?

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hello Sean, I am pasting what I answered in your support ticket on this question for anyone else having a similar query. Once we reach a conclusion in the private case, we can post the solution here too. You can bind parameters to fields of the view model of the component. You can change those as needed, and the change will reflect in the buttons rendering. To hide buttons, simply wrap them in an if-block based on the view model values. If this does not work for you, could you post a snippet to showcase the Telerik Button problem so I can offer a more concrete answer? Regards, Marin Bratanov
