# Popup list width issue with a multi-select

## Question

**Bob** asked on 17 Feb 2020

So I am currently running into an issue where, if I set the Width property of a TelerikMultiSelect to 100%, then the popup list spans the entire width of the browser window. As I found this is because the popup list is being appended to the body (well, close to the body) of the DOM and not to the parent widget (in this case a div with the class k-multiselect). Is there a way to make the popup list match the width of the multiselect, if I set the Width property to 100%?

## Answer

**Marin Bratanov** answered on 17 Feb 2020

Hi Bobby, Please Follow the implementation of this feature in this page (I added your Vote for it on your behalf): [https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set](https://feedback.telerik.com/blazor/1440092-dropdown-components-to-calculate-their-dropdown-element-width-to-match-the-actual-width-of-the-component-in-px-when-popupwidth-is-not-set) Regards, Marin Bratanov
