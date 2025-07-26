# Open Dialog from Modal Window

## Question

**Mar** asked on 09 Apr 2021

I am opening the dialog from a modal window is there a way to have the dialog disable/turn grey the modal window as well as the page. With the way it works now you can keep entering data on the modal window.

## Answer

**Mark** answered on 12 Apr 2021

I started working on making a sample application showing the problem but I was unable to reproduce the problem in a sample app build from the telerik template. So I started looking at what was different and I found that if I add the following CSS to my application it works as expect. I really don't understand css well enough but I have a fix so I am all set. #app { display: flex; flex-direction: column; }

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hi Mark, Indeed, We've been able to reproduce this behavior, and it does come when the parent element of the dialogs does not have display: flex. I made this page in our Feedback Portal where you can Follow the fix for this: [https://feedback.telerik.com/blazor/1515146-predefined-dialogs-don-t-cover-a-modal-dialog-when-the-telerikrootcomponent-parent-does-not-have-display-flex](https://feedback.telerik.com/blazor/1515146-predefined-dialogs-don-t-cover-a-modal-dialog-when-the-telerikrootcomponent-parent-does-not-have-display-flex) Regards, Marin Bratanov
