# Preselected text in input on Incell edit mode

## Question

**Cip** asked on 24 Nov 2020

Hi guys, Is there a possibility in incell edit mode, on edit, when a text/numeric input shows up, from the EditTemplate, it's text to be selected by default? What I want to achieve is the following: in a numeric input we have the default value of zero. I want that value to be selected as when the user does a copy+paste in the input that value will be overwritten. If it's not selected the cursor appears after that value so when the user does a copy+paste then the new value will be concatenated with the value that was present in the input before the copy+paste, which is an issue that I don't want to achieve. I hope you understood what I want to achieve. Best regards, Cipri

## Answer

**Marin Bratanov** answered on 24 Nov 2020

Hi Cipri, You can Follow the implementation of such a built-in feature for the numeric tetbox here: [https://feedback.telerik.com/blazor/1454982-always-highlight-all-numerictextbox-content-on-focus.](https://feedback.telerik.com/blazor/1454982-always-highlight-all-numerictextbox-content-on-focus.) The thread also offers a solution you can use for the time being. Regards, Marin Bratanov
